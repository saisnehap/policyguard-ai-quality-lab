from google import genai

def main():
    client = genai.Client()

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=(
            "You are a fictional store support assistant. "
            "Policy: Standard shipping takes 3 to 5 business days. "
            "Question: How long does standard shipping take? "
            "Answer briefly using only the policy."
        )
    )

    print(response.output_text)

if __name__ == "__main__":
    main()