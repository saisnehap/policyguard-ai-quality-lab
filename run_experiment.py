
from policyguard.faulty_inventory import (
    FaultyInventory,
    DoubleReservationInventory,
    WrongProductInventory,
)
from policyguard.evaluators import (
    evaluate_response,
    evaluate_state,
)
from policyguard.metrics import fault_detection_rate


faulty_implementations = [
    FaultyInventory,
    DoubleReservationInventory,
    WrongProductInventory,
]

response_detected = 0
state_detected = 0

for inventory_class in faulty_implementations:
    inventory = inventory_class()

    initial_stock = inventory.check_stock("laptop")
    result = inventory.reserve_stock("laptop", 3)
    final_stock = inventory.check_stock("laptop")

    response_passed = evaluate_response(result)
    state_passed = evaluate_state(
        initial_stock, 3, final_stock
    )

    if not response_passed:
        response_detected += 1

    if not state_passed:
        state_detected += 1

    print(
        f"{inventory_class.__name__}: "
        f"Response={'PASS' if response_passed else 'FAIL'}, "
        f"State={'PASS' if state_passed else 'FAIL'}"
    )

total = len(faulty_implementations)

print("\n--- Evaluator Effectiveness ---")
print(
    "Response-only detection:",
    fault_detection_rate(response_detected, total),
    "%"
)
print(
    "State-aware detection:",
    fault_detection_rate(state_detected, total),
    "%"
)
