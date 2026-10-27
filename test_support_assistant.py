import pytest

from read_policies import load_policies
from support_assistant import retrieve_policies
from unittest.mock import Mock

from support_assistant import answer_question



@pytest.fixture
def policies():
    return load_policies("data/store_policies.json")


@pytest.mark.parametrize(
    "question, expected_ids",
    [
        ("Can I return my purchase?", ["returns_v1"]),
        ("When will my order arrive?", ["shipping_v1"]),
        ("CANCEL my order please", ["cancellations_v1"]),
        ("Do you offer warranties?", []),
        (
            "Can I cancel before delivery?",
            ["shipping_v1", "cancellations_v1"]
        )
    ]
)
def test_retrieve_policies(policies, question, expected_ids):
    matches = retrieve_policies(question, policies)
    actual_ids = [policy["id"] for policy in matches]

    assert actual_ids == expected_ids




def test_shipping_answer_uses_retrieved_policy():
    policies = [
        {
            "id": "shipping_v1",
            "topic": "shipping",
            "text": "Standard shipping takes 3 to 5 business days."
        },
        {
            "id": "returns_v1",
            "topic": "returns",
            "text": "Unused items may be returned within 30 days."
        }
    ]

    client = Mock()
    client.interactions.create.return_value.output_text = (
        "Shipping takes 3 to 5 business days. [shipping_v1]"
    )

    answer = answer_question("How long does shipping take?", policies, client)

    client.interactions.create.assert_called_once()

    prompt = client.interactions.create.call_args.kwargs["input"]
    assert policies[0]["text"] in prompt
    assert policies[1]["text"] not in prompt
    assert answer == "Shipping takes 3 to 5 business days. [shipping_v1]"

def test_unknown_topic_does_not_call_gemini():
    client = Mock()

    answer = answer_question(
        "Do you offer gift wrapping?",
        [],
        client
    )

    assert answer == "I don't have a policy that answers this question."
    client.interactions.create.assert_not_called()


def test_api_timeout_returns_friendly_message():
    policies = [
        {
            "id": "shipping_v1",
            "topic": "shipping",
            "text": "Standard shipping takes 3 to 5 business days."
        }
    ]

    client = Mock()
    client.interactions.create.side_effect = TimeoutError(
        "Simulated timeout"
    )

    answer = answer_question(
        "When will my delivery arrive?",
        policies,
        client
    )

    assert answer == (
        "The assistant is temporarily unavailable. Please try again."
    )
    client.interactions.create.assert_called_once()
