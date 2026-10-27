import json

def load_policies(path):
    with open(path, "r", encoding="utf-8") as file:
        policies = json.load(file)

    required_fields = ["id", "topic", "text"]

    for policy in policies:
        for field in required_fields:
            if field not in policy:
                raise ValueError(f"Policy is missing {field}")

    return policies

if __name__ == "__main__":
    policies = load_policies("data/store_policies.json")
    print(len(policies))

    for policy in policies:
        print(policy["id"])    

        