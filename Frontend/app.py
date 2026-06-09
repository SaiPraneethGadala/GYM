import streamlit as st
import sys
import os

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
# SIDEBAR
# ----------------------------------
with st.sidebar:

    st.header("⚙️ Settings")

    st.info(
        "Answers are generated using the gym PDF knowledge base."
    )

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
# DISPLAY CHAT
# ----------------------------------
for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )

# ----------------------------------
# USER INPUT
# ----------------------------------
user_input = st.chat_input(
    "Ask about workouts, diet, membership, timings..."
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

    # Build conversation history
    history = "\n".join([
        f"{m['role']}: {m['content']}"
        for m in st.session_state.messages[-10:]
    ])

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = gym_rag(
                    query=user_input,
                    history=history
                )

            except Exception as e:

                response = (
                    f"Error: {str(e)}"
                )

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
