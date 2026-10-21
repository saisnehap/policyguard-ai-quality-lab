household = {
    "size": 3,
    "state": "NM",
    "income": 45000
}

def get_income(data):
    return data["income"]

print(get_income(household))

def summarize_household(data):
    if data["size"] == 1:
        return f"{data['state']}: {data['size']} person"
    else:
        return f"{data['state']}: {data['size']} people"

print(summarize_household(household))
