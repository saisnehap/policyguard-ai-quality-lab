
import pytest

from policyguard.metrics import fault_detection_rate


def test_all_faults_detected():
    assert fault_detection_rate(3, 3) == 100.0


def test_no_faults_detected():
    assert fault_detection_rate(0, 3) == 0.0


def test_partial_detection():
    assert fault_detection_rate(2, 4) == 50.0


def test_zero_total_rejected():
    with pytest.raises(ValueError):
        fault_detection_rate(0, 0)


def test_invalid_detected_count_rejected():
    with pytest.raises(ValueError):
        fault_detection_rate(4, 3)
