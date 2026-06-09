def classify_query(query):
    q = query.lower()

    if any(x in q for x in [
        "workout",
        "exercise",
        "training",
        "strength"
    ]):
        return "WORKOUT"

    if any(x in q for x in [
        "diet",
        "meal",
        "nutrition"
    ]):
        return "DIET"

    if any(x in q for x in [
        "membership",
        "fee",
        "price",
        "cost"
    ]):
        return "MEMBERSHIP"

    if any(x in q for x in [
        "timing",
        "hours",
        "open",
        "close"
    ]):
        return "TIMINGS"

    return "GENERAL"