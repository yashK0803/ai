KNOWLEDGE_BASE = [
    {
        "name": "Library Management System",
        "conditions": {
            "data_type": "books",
            "users": "many",
            "security": "medium",
            "access": "search",
        },
        "explanation": (
            "Chosen for handling book records, multiple users, "
            "catalog search, and moderate security needs."
        ),
    },

    {
        "name": "Hospital Information System",
        "conditions": {
            "data_type": "medical",
            "users": "many",
            "security": "high",
            "access": "update",
        },
        "explanation": (
            "Chosen for sensitive medical records that need high "
            "security and regular updates by many users."
        ),
    },

    {
        "name": "Student Information System",
        "conditions": {
            "data_type": "student",
            "users": "many",
            "security": "medium",
            "access": "update",
        },
        "explanation": (
            "Chosen for student records, many users, "
            "and regular academic data updates."
        ),
    },

    {
        "name": "Office Document Management System",
        "conditions": {
            "data_type": "documents",
            "users": "few",
            "security": "medium",
            "access": "store",
        },
        "explanation": (
            "Chosen for managing office files and documents "
            "with controlled internal access."
        ),
    },
]


QUESTIONS = [
    (
        "data_type",
        "What type of data do you manage? "
        "(books / medical / student / documents): "
    ),

    (
        "users",
        "How many users access the system? (few / many): "
    ),

    (
        "security",
        "What security level is required? "
        "(low / medium / high): "
    ),

    (
        "access",
        "What is the main operation? "
        "(search / update / store): "
    ),
]


def ask_user():
    facts = {}

    print("Expert System: Information Management")
    print("Answer the following questions:\n")

    for key, question in QUESTIONS:
        facts[key] = input(question).strip().lower()

    return facts


def infer_system(facts):
    best_match = None
    best_score = -1
    matched_rules = []

    for rule in KNOWLEDGE_BASE:
        score = 0
        current_matches = []

        for key, expected_value in rule["conditions"].items():
            if facts.get(key) == expected_value:
                score += 1
                current_matches.append(f"{key} = {expected_value}")

        if score > best_score:
            best_score = score
            best_match = rule
            matched_rules = current_matches

    return best_match, matched_rules, best_score


def explain_decision(system_rule, matched_rules, score):
    print("\nExplanation Facility")

    print(f"Recommended System: {system_rule['name']}")

    print(f"Matched Rule Count: {score}")

    print("Reasoning:")

    for rule in matched_rules:
        print(f"- {rule}")

    print(f"Justification: {system_rule['explanation']}")


def main():
    user_facts = ask_user()

    system_rule, matched_rules, score = infer_system(user_facts)

    print("\nInference Engine Result")

    print(
        "The suggested information management solution is: "
        f"{system_rule['name']}"
    )

    explain_decision(system_rule, matched_rules, score)


if __name__ == "__main__":
    main()