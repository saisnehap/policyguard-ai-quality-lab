from google import genai

from read_policies import load_policies
from support_assistant import answer_question


def main():
    policies = load_policies("data/store_policies.json")
    client = genai.Client()

    question = "How long does shipping take?"
    answer = answer_question(question, policies, client)

    print("Question:", question)
    print("Answer:", answer)


if __name__ == "__main__":
    main()