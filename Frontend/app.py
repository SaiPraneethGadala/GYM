import streamlit as st
import sys
import os

# ----------------------------------
# STREAMLIT SECRETS
# ----------------------------------
HUGGINGFACE_API_KEY = st.secrets["HUGGINGFACE_API_KEY"]
MODEL_NAME = st.secrets["MODEL_NAME"]
EMBEDDING_MODEL = st.secrets["EMBEDDING_MODEL"]

# ----------------------------------
# IMPORT BACKEND
# ----------------------------------
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from Backend.gym_rag import gym_rag

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="Gym AI Chatbot",
    page_icon="🏋️",
    layout="wide"
)

# ----------------------------------
# HEADER
# ----------------------------------
st.title("🏋️ Gym AI Chatbot")
st.caption("Your Personal Fitness Assistant 💪")

# ----------------------------------
# SIDEBAR
# ----------------------------------
with st.sidebar:

    st.header("⚙️ Settings")

    st.success("Gym AI is running")

    st.write(f"Model: {MODEL_NAME}")

    if st.button("🧹 Clear Chat"):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content":
                "Chat cleared. How can I help you today? 💪"
            }
        ]

        st.rerun()

# ----------------------------------
# CHAT MEMORY
# ----------------------------------
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            "Hi! I'm Gym AI 💪. Ask me about workouts, diet plans, memberships, or gym timings."
        }
    ]

# ----------------------------------
# DISPLAY CHAT
# ----------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )

# ----------------------------------
# USER INPUT
# ----------------------------------
user_input = st.chat_input(
    "Ask about workouts, diet plans, memberships, gym timings..."
)

# ----------------------------------
# PROCESS QUERY
# ----------------------------------
if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)

    history = "\n".join([
        f"{msg['role']}: {msg['content']}"
        for msg in st.session_state.messages[-10:]
    ])

    with st.chat_message("assistant"):

        with st.spinner("Thinking... 💭"):

            try:

                response = gym_rag(
                    query=user_input,
                    history=history
                )

            except Exception as e:

                response = (
                    f"❌ Error: {str(e)}"
                )

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
