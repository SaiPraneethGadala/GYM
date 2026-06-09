from langchain_huggingface import HuggingFaceEmbeddings
import streamlit as st


@st.cache_resource
def load_embeddings():
    """
    Load MiniLM embedding model once and cache it.
    """

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )


# Global embedding object
embedder = load_embeddings()
