🚀 Live Demo

Try the application here:

https://7peeuc4hy9ogmuicsftznj.streamlit.app/

# 🏋️ Gym AI Chatbot

Gym AI Chatbot is a Retrieval-Augmented Generation (RAG) based fitness assistant that answers questions about workouts, diet plans, gym memberships, and gym timings using information stored in PDF documents.

## Features

* 💪 Workout plan recommendations
* 🥗 Diet and nutrition guidance
* 🏋️ Membership information
* ⏰ Gym timings and schedules
* 📄 PDF-based knowledge retrieval
* 🤖 AI-powered conversational interface
* 🌐 Streamlit web application

## Project Structure

```text
TAG_GYM/
│
├── Backend/
│   ├── embeddings.py
│   ├── retriever.py
│   ├── gym_rag.py
│   ├── llm.py
│   ├── classifier.py
│   ├── memory.py
│   ├── prompts.py
│   └── main.py
│
├── Data/
│   ├── diet_plans.pdf
│   ├── gym_timings.pdf
│   ├── membership_plans.pdf
│   └── workout_plans.pdf
│
├── Frontend/
│   └── app.py
│
├── requirements.txt
├── runtime.txt
└── README.md
```

## Technologies Used

* Python
* Streamlit
* LangChain
* FAISS
* Hugging Face Embeddings
* Sentence Transformers
* PyPDF
* NumPy

## Installation

### Clone Repository

```bash
git clone https://github.com/SaiPraneethGadala/GYM.git
cd GYM
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
HUGGINGFACE_API_KEY=YOUR_HUGGINGFACE_TOKEN
MODEL_NAME=google/flan-t5-large
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

For Streamlit Cloud deployment, add these values under **App Settings → Secrets**.

## Run Application

```bash
streamlit run Frontend/app.py
```

## Example Questions

* What membership plans are available?
* What is the beginner workout plan?
* Give me a diet plan.
* What are the gym timings?
* What workout is best for muscle gain?
* What are the membership fees?

## Deployment

### Streamlit Cloud

1. Push project to GitHub.
2. Create a new Streamlit Cloud app.
3. Select repository and branch.
4. Set:

   * Python Version: 3.11
   * Main File: `Frontend/app.py`
5. Add secrets:

   * HUGGINGFACE_API_KEY
   * MODEL_NAME
   * EMBEDDING_MODEL
6. Deploy.

## Future Improvements

* User authentication
* Personalized workout plans
* Voice assistant support
* Progress tracking
* Advanced nutrition recommendations
* Mobile application

## Author

**Sai Praneeth Gadala**

Final Year B.Tech (AI & ML)

Gym AI Chatbot Project
