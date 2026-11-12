
import json
from datetime import datetime, timezone
from pathlib import Path

from policyguard.inventory import Inventory
from policyguard.faulty_inventory import (
    FaultyInventory,
    DoubleReservationInventory,
    WrongProductInventory,
    UnauthorizedActionInventory,
)
from policyguard.evaluators import (
    evaluate_response,
    evaluate_state,
    evaluate_actions,
)

SCENARIOS = [
    ("correct", Inventory, True),
    ("false_success", FaultyInventory, False),
    ("double_reservation", DoubleReservationInventory, False),
    ("wrong_product", WrongProductInventory, False),
    ("unauthorized_action", UnauthorizedActionInventory, False),
]


def run_scenario(name, inventory_class, expected_valid):
    inventory = inventory_class()

    initial = inventory.get_inventory_state()
    result = inventory.reserve_stock("laptop", 3)
    final = inventory.get_inventory_state()

    actions = getattr(inventory, "actions", [])

    response_pass = evaluate_response(result)

    # Compare the full inventory, not only laptop stock.
    expected_final = initial.copy()
    expected_final["laptop"] -= 3
    state_pass = result is True and final == expected_final

    action_pass = evaluate_actions(actions)

    # Combined evaluator requires state and action correctness.
    combined_pass = response_pass and state_pass and action_pass

    return {
        "scenario": name,
        "expected_valid": expected_valid,
        "response_pass": response_pass,
        "state_pass": state_pass,
        "combined_pass": combined_pass,
        "initial_state": initial,
        "final_state": final,
        "actions": actions,
    }


def calculate_metrics(results, evaluator_key):
    faulty = [r for r in results if not r["expected_valid"]]
    valid = [r for r in results if r["expected_valid"]]

    detected = sum(not r[evaluator_key] for r in faulty)
    false_alarms = sum(not r[evaluator_key] for r in valid)

    return {
        "fault_detection_rate": round(100 * detected / len(faulty), 2),
        "false_positive_rate": round(
            100 * false_alarms / len(valid), 2
        ),
        "faults_detected": detected,
        "faults_total": len(faulty),
    }


def main():
    results = [
        run_scenario(name, cls, expected_valid)
        for name, cls, expected_valid in SCENARIOS
    ]

    metrics = {
        key: calculate_metrics(results, key)
        for key in (
            "response_pass",
            "state_pass",
            "combined_pass",
        )
    }

    report = {
        "project": "PolicyGuard AI Agent Evaluation Confidence Lab",
        "experiment": "Synthetic evaluator oracle audit",
        "generated_at_utc": datetime.now(
            timezone.utc
        ).isoformat(),
        "scenarios": results,
        "metrics": metrics,
        "limitations": [
            "Uses synthetic inventory behavior, not a real LLM.",
            "Faults were manually selected.",
            "Action checks use simplified action labels.",
            "Results do not establish real-world model performance.",
        ],
    }

    output = Path("reports/evaluation_report.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )

    print(f"Report created: {output}")
    print("\nEvaluator comparison:")
    for name, values in metrics.items():
        print(
            f"{name}: "
            f"{values['faults_detected']}/"
            f"{values['faults_total']} faults detected; "
            f"detection rate="
            f"{values['fault_detection_rate']}%"
        )


if __name__ == "__main__":
    main()
