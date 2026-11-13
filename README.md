
# PolicyGuard — AI Agent Evaluation Confidence Lab

A Python-based evaluation testing framework that investigates
how effectively software test oracles detect failures in
stateful AI-agent-style workflows.

Built with Python, Pytest, synthetic fault injection,
and automated regression testing.

## Overview

AI-agent workflows can appear successful while underlying
actions or system states are incorrect.

PolicyGuard explores a fundamental quality engineering question:

**Can an evaluation framework reliably distinguish correct
behavior from defective behavior?**

The current prototype uses a synthetic inventory simulator
to test different evaluation strategies against known faults.

## Key Features

- Synthetic inventory simulation
- Controlled fault injection
- Response-only evaluation
- Final-state validation
- Action-invariant evaluation
- False-positive and false-negative demonstrations
- Fault-detection metrics
- JSON experiment reports
- Automated Pytest regression tests
- GitHub Actions CI/CD

## Architecture

```text
policyguard-ai-quality-lab/
├── policyguard/
│   ├── __init__.py
│   ├── inventory.py
│   ├── faulty_inventory.py
│   ├── evaluators.py
│   └── metrics.py
├── tests/
│   ├── test_inventory.py
│   ├── test_evaluators.py
│   └── test_metrics.py
├── reports/
│   └── evaluation_report.json
├── run_experiment.py
├── generate_report.py
└── .github/workflows/
    └── python-tests.yml
```

Additional Python learning exercises and tests remain
in the repository.

## Evaluation Strategies

| Evaluation Strategy | Description |
|---|---|
| Response-only | Checks whether the tool reports success |
| State-aware | Checks whether the expected inventory state was produced |
| Combined | Validates response, system state, and prohibited actions |

## Experimental Results

Four deliberately introduced faults were evaluated.

| Evaluator | Faults Detected | Detection Rate |
|---|---:|---:|
| Response-only | 0/4 | 0% |
| State-aware | 3/4 | 75% |
| Combined | 4/4 | 100% |

The combined evaluator detected all four faults in
this controlled experiment.

**Note:** These results reflect four hand-designed synthetic
faults, not real-world LLM-agent performance.

## Fault Injection Scenarios

1. **False success:** Tool returns success without updating stock.
2. **Double reservation:** Tool deducts inventory twice.
3. **Wrong product:** Tool modifies a different inventory item.
4. **Unauthorized action:** Tool performs a prohibited intermediate action.

These scenarios demonstrate why checking only a tool response
or final state may miss important failures.

## Technology Stack

- Python
- Pytest
- JSON
- GitHub Actions
- Git

## Getting Started

Clone the repository:

```bash
git clone https://github.com/saisnehap/policyguard-ai-quality-lab.git
cd policyguard-ai-quality-lab
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install pytest
```

Run all automated tests:

```bash
python -m pytest -q
```

Run the evaluator experiment:

```bash
python run_experiment.py
```

Generate the evaluation report:

```bash
python generate_report.py
```

The generated report is saved at:

`reports/evaluation_report.json`

## Continuous Integration

GitHub Actions automatically runs regression tests,
generates the evaluation report, validates the JSON output,
and uploads the report as a workflow artifact.

## Current Limitations

- Uses synthetic deterministic workflows rather than real
  LLM-generated agent executions.
- Evaluates a small, manually constructed set of faults.
- Action evaluation uses simplified action labels.
- The current experiment includes only one known-valid
  scenario, limiting false-positive analysis.
- The results do not establish superiority over existing
  AI evaluation frameworks.

## Future Research

Planned enhancements include:

- Real LLM tool-calling integration
- Structured action traces
- Expanded fault injection datasets
- False-positive and false-negative measurement
- Evaluator quality regression gates
- Comparative evaluation experiments
- Reproducible research benchmarks

## Project Status

**v0.1.0 — Experimental MVP (Pre-release)**

The current release demonstrates evaluator quality auditing
through synthetic fault injection and automated testing.
