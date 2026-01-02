import re

def normalize(text):
    text = text.lower()
    return re.sub(r"[^a-z0-9\s]", "", text)

def score_answer(user_answer, expected_points):
    user_answer = normalize(user_answer)

    matched, missed = [], []

    for point in expected_points:
        point_norm = normalize(point)
        keywords = point_norm.split()

        if any(word in user_answer for word in keywords):
            matched.append(point)
        else:
            missed.append(point)

    score = int((len(matched) / len(expected_points)) * 100)

    return {
        "score": score,
        "matched": matched,
        "missed": missed
    }
