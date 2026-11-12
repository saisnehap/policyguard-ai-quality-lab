
def fault_detection_rate(detected_faults, total_faults):
    """Calculate the percentage of injected faults detected."""

    if total_faults <= 0:
        raise ValueError("Total faults must be greater than zero")

    if not 0 <= detected_faults <= total_faults:
        raise ValueError("Invalid detected faults count")

    return (detected_faults / total_faults) * 100
