from read_policies import load_policies
import pytest
import json 

def test_load_store_policies():
    policies = load_policies("data/store_policies.json")

    assert len(policies) == 3
    assert policies[0]["id"] == "returns_v1"

def test_load_another_policy_file(tmp_path):
    policy_file = tmp_path / "policies.json"
    policy_file.write_text(
        '[{"id": "demo_v1", "topic": "demo", "text": "Example policy."}]',
        encoding="utf-8"
    )

    policies = load_policies(policy_file)

    assert len(policies) == 1
    assert policies[0]["id"] == "demo_v1"    


def test_reject_policy_missing_text(tmp_path):
    policy_file = tmp_path / "invalid.json"
    policy_file.write_text(
        '[{"id": "returns_v1", "topic": "returns"}]',
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="missing text"):
        load_policies(policy_file)   


def test_reject_missing_text_in_second_policy(tmp_path):
    policy_file = tmp_path / "policies.json"
    policy_file.write_text(
        '[{"id": "a", "topic": "returns", "text": "Example"},'
        ' {"id": "b", "topic": "shipping"}]',
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="missing text"):
        load_policies(policy_file)      

@pytest.mark.parametrize("field", ["id", "topic", "text"])
def test_reject_missing_required_field(tmp_path, field):
    policy = {
        "id": "demo_v1",
        "topic": "returns",
        "text": "Example policy."
    }
    del policy[field]

    policy_file = tmp_path / "policy.json"
    policy_file.write_text(
        json.dumps([policy]),
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match=f"missing {field}"):
        load_policies(policy_file)         