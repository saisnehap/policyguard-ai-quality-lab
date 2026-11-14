import json

with open("households.json", "r") as file:
    households = json.load(file)

print(households[0]["state"])


