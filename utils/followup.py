import json, random

def get_followup(topic, missed_points):
    with open("data/followup_questions.json") as f:
        followups = json.load(f)

    topic_map = followups.get(topic, {})
    candidates = []

    for miss in missed_points:
        for key in topic_map:
            if key.lower() in miss.lower():
                candidates.append(topic_map[key])

    if candidates:
        return random.choice(candidates)

    return "Can you explain this concept in more detail?"
