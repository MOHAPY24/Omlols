from fuzzywuzzy import fuzz

def user_mentions_source(user_text, sources, threshold=60):
    for source in sources:
        name = source["name"]
        score = fuzz.partial_ratio(name.lower(), user_text.lower())
        if score >= threshold:
            return True
    return False
