def get_history(messages, k=6):
    history = messages[-k:]

    return "\n".join(
        f"{m['role']}: {m['content']}"
        for m in history
    )