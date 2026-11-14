prompts = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'The Arrival'."
]

for prompt in prompts:
    print(prompt)
    print_llm_response(prompt)