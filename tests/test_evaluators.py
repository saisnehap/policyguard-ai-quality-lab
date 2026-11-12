
from policyguard.inventory import Inventory
from policyguard.faulty_inventory import FaultyInventory
from policyguard.evaluators import (
    evaluate_response,
    evaluate_state,
)


def test_correct_inventory_passes_both_evaluators():
    inventory = Inventory()

    initial_stock = inventory.check_stock("laptop")
    result = inventory.reserve_stock("laptop", 3)
    final_stock = inventory.check_stock("laptop")

    assert evaluate_response(result) is True

    assert evaluate_state(
        initial_stock, 3, final_stock
    ) is True


def test_faulty_inventory_exposes_weak_evaluator():
    inventory = FaultyInventory()

    initial_stock = inventory.check_stock("laptop")
    result = inventory.reserve_stock("laptop", 3)
    final_stock = inventory.check_stock("laptop")

    # Weak evaluator incorrectly accepts the operation.
    assert evaluate_response(result) is True

    # State-aware evaluator correctly rejects the operation.
    assert evaluate_state(
        initial_stock, 3, final_stock
    ) is False



import pytest

from policyguard.faulty_inventory import (
    DoubleReservationInventory,
    WrongProductInventory,
)


@pytest.mark.parametrize(
    "inventory_class",
    [
        FaultyInventory,
        DoubleReservationInventory,
        WrongProductInventory,
    ],
)
def test_evaluators_against_injected_faults(inventory_class):
    inventory = inventory_class()

    initial_stock = inventory.check_stock("laptop")
    result = inventory.reserve_stock("laptop", 3)
    final_stock = inventory.check_stock("laptop")

    # Weak evaluator misses these faults.
    assert evaluate_response(result) is True

    # State-aware evaluator detects them.
    assert evaluate_state(
        initial_stock, 3, final_stock
    ) is False


from policyguard.faulty_inventory import UnauthorizedActionInventory
from policyguard.evaluators import evaluate_actions


def test_state_only_evaluator_misses_unauthorized_action():
    inventory = UnauthorizedActionInventory()

    initial_stock = inventory.check_stock("laptop")
    result = inventory.reserve_stock("laptop", 3)
    final_stock = inventory.check_stock("laptop")

    # Tool claims success.
    assert evaluate_response(result) is True

    # Final state appears correct.
    assert evaluate_state(
        initial_stock, 3, final_stock
    ) is True

    # Action-aware evaluator catches prohibited behavior.
    assert evaluate_actions(inventory.actions) is False

    # Verify the final mouse stock was restored.
    assert inventory.check_stock("mouse") == 20


from policyguard.evaluators import evaluate_strict_sequence


def test_strict_evaluator_accepts_expected_sequence():
    actions = ["check_stock", "reserve"]

    assert evaluate_strict_sequence(actions) is True
    assert evaluate_actions(actions) is True


def test_strict_evaluator_rejects_valid_alternative():
    # The reserve operation already validates stock internally.
    actions = ["reserve"]

    # Strict evaluator incorrectly rejects valid behavior.
    assert evaluate_strict_sequence(actions) is False

    # Our action-invariant evaluator permits this sequence.
    assert evaluate_actions(actions) is True
