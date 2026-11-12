
def evaluate_response(result):
    """
    Weak evaluator:
    Checks only whether the action returned True.
    """
    return result is True


def evaluate_state(initial_stock, reserved_quantity, final_stock):
    """
    State-aware evaluator:
    Checks whether inventory changed correctly.
    """
    expected_stock = initial_stock - reserved_quantity

    return final_stock == expected_stock


def evaluate_actions(actions):
    """
    Reject executions containing prohibited actions.
    """
    prohibited_actions = {"unauthorized_modify_mouse"}

    return not any(
        action in prohibited_actions
        for action in actions
    )


def evaluate_strict_sequence(actions):
    """
    An intentionally strict evaluator.

    Requires an exact sequence of actions.
    """
    expected_actions = ["check_stock", "reserve"]

    return actions == expected_actions
