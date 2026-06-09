from .gym_rag import gym_rag

def chatbot(query, history=""):
    return gym_rag(
        query=query,
        history=history
    )