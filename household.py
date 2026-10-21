household = {
    "size": 3,
    "state": "NM",
    "income": 45000
}

def get_income(data):
    return data["income"]

print(get_income(household))