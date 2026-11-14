import json
from datetime import datetime, timezone
from pathlib import Path

from google import genai

from read_policies import load_policies
from support_assistant import answer_question


def main():
    policies = load_policies("data/store_policies.json")

    with open("data/eval_cases.json", encoding="utf-8") as file:
        cases = json.load(file)

    client = genai.Client()
    results = []

    for case in cases:
        print(f"Running: {case['id']}", flush=True)

        answer = answer_question(
            case["question"],
            policies,
            client
        )
        print(f"Answer received: {answer}", flush=True)

        results.append({
            "id": case["id"],
            "category": case["category"],
            "question": case["question"],
            "expected_behavior": case["expected_behavior"],
            "actual_answer": answer,
            "review_status": "pending",
            "review_notes": ""
        })

    report = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "results": results
    }

    output_folder = Path("reports")
    output_folder.mkdir(exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    output_path = output_folder / f"evaluation_{timestamp}.json"

    output_path.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8"
    )

    print(f"Saved {len(results)} results to {output_path}")


if __name__ == "__main__":
    main()