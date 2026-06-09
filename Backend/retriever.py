import numpy as np
import faiss
from pathlib import Path
from pypdf import PdfReader

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ----------------------------------
# RETRIEVER
# ----------------------------------
class Retriever:
    def __init__(self, index, documents, embedder):
        self.index = index
        self.documents = documents
        self.embedder = embedder

    def retrieve(self, query, top_k=5):

        query_embedding = self.embedder.embed_query(query)

        query_embedding = np.array(
            [query_embedding],
            dtype="float32"
        )

        faiss.normalize_L2(query_embedding)

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:
            if idx != -1:
                results.append(
                    self.documents[idx]
                )

        return results


# ----------------------------------
# PDF LOADER
# ----------------------------------
def extract_pdf(pdf_path):

    reader = PdfReader(str(pdf_path))

    pages = []

    for page_num, page in enumerate(
        reader.pages,
        start=1
    ):

        text = page.extract_text() or ""

        if text.strip():

            pages.append({
                "source": pdf_path.name,
                "page": page_num,
                "text": text
            })

    return pages


# ----------------------------------
# BUILD RETRIEVER
# ----------------------------------
def get_retriever(data_dir):

    data_path = Path(data_dir)

    if not data_path.exists():
        raise Exception(
            f"Data folder not found: {data_dir}"
        )

    pdf_files = list(
        data_path.glob("*.pdf")
    )

    if not pdf_files:
        raise Exception(
            "No PDF files found."
        )

    raw_pages = []

    for pdf in pdf_files:

        pages = extract_pdf(pdf)

        print(
            f"{pdf.name} → {len(pages)} pages extracted"
        )

        raw_pages.extend(pages)

    if not raw_pages:
        raise Exception(
            "No text found in PDFs."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for page in raw_pages:

        split_texts = splitter.split_text(
            page["text"]
        )

        for chunk in split_texts:

            chunks.append({
                "source": page["source"],
                "page": page["page"],
                "text": chunk
            })

    print(
        f"Total chunks: {len(chunks)}"
    )

    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = embedder.embed_documents(
        texts
    )

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    faiss.normalize_L2(
        embeddings
    )

    print(
        "Embedding shape:",
        embeddings.shape
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(
        dimension
    )

    index.add(
        embeddings
    )

    return Retriever(
        index=index,
        documents=chunks,
        embedder=embedder
    )