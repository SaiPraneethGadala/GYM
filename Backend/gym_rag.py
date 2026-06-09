import os
from .retriever import get_retriever

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "data")
)

print("Loading data from:", DATA_PATH)

retriever = get_retriever(DATA_PATH)


def detect_category(query):
    q = query.lower()

    if any(word in q for word in [
        "workout",
        "exercise",
        "training",
        "strength",
        "muscle",
        "fitness"
    ]):
        return "workout"

    if any(word in q for word in [
        "diet",
        "meal",
        "nutrition",
        "food"
    ]):
        return "diet"

    if any(word in q for word in [
        "membership",
        "fee",
        "fees",
        "price",
        "cost",
        "subscription",
        "plan"
    ]):
        return "membership"

    if any(word in q for word in [
        "timing",
        "timings",
        "hours",
        "open",
        "close"
    ]):
        return "gym"

    return None


def format_response(query, docs):

    if not docs:
        return "Information not found in gym data."

    answer = ""

    if "membership" in query.lower():
        answer += "🎫 Membership Information\n\n"

    elif "diet" in query.lower():
        answer += "🥗 Diet Plan Information\n\n"

    elif any(word in query.lower() for word in [
        "workout",
        "exercise",
        "training"
    ]):
        answer += "💪 Workout Plan Information\n\n"

    elif any(word in query.lower() for word in [
        "timing",
        "hours",
        "open",
        "close"
    ]):
        answer += "⏰ Gym Timing Information\n\n"

    used_text = []

    for doc in docs:

        text = doc["text"].strip()

        if text not in used_text:
            answer += text + "\n\n"
            used_text.append(text)

    return answer.strip()


def gym_rag(query, history=""):

    query_lower = query.lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    ]

    if query_lower in greetings:

        return (
            "Hello! 👋 I'm Gym AI.\n\n"
            "I can help you with:\n"
            "• Workout Plans 💪\n"
            "• Diet Plans 🥗\n"
            "• Membership Details 🎫\n"
            "• Gym Timings ⏰\n\n"
            "Ask me anything about the gym."
        )

    try:

        docs = retriever.retrieve(
            query=query,
            top_k=8
        )

        category = detect_category(query)

        if category:

            filtered_docs = [
                doc for doc in docs
                if category in doc["source"].lower()
            ]

            if filtered_docs:
                docs = filtered_docs

        if not docs:
            return "Information not found in gym data."

        return format_response(
            query,
            docs
        )

    except Exception as e:
        return f"Error: {str(e)}"