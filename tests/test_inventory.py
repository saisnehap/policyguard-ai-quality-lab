
import pytest

from policyguard.inventory import Inventory


@pytest.fixture
def inventory():
    return Inventory()


def test_initial_stock(inventory):
    assert inventory.check_stock("laptop") == 10


def test_successful_reservation(inventory):
    result = inventory.reserve_stock("laptop", 3)

    assert result is True
    assert inventory.check_stock("laptop") == 7


def test_insufficient_stock(inventory):
    result = inventory.reserve_stock("laptop", 15)

    assert result is False
    assert inventory.check_stock("laptop") == 10


def test_invalid_quantity(inventory):
    result = inventory.reserve_stock("laptop", -2)

    assert result is False
    assert inventory.check_stock("laptop") == 10


def test_unknown_product(inventory):
    result = inventory.reserve_stock("tablet", 2)

    assert result is False
    assert "tablet" not in inventory.get_inventory_state()


def test_inventory_state_is_independent_copy(inventory):
    state = inventory.get_inventory_state()
    state["laptop"] = 999

    assert inventory.check_stock("laptop") == 10



from policyguard.faulty_inventory import FaultyInventory


def test_detect_false_success():
    faulty = FaultyInventory()

    result = faulty.reserve_stock("laptop", 3)

    # The faulty tool claims the reservation succeeded.
    assert result is True

    # Our evaluator checks the actual system state.
    assert faulty.check_stock("laptop") != 7
