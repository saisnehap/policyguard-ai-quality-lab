# PolicyGuard AI Quality Lab

A personal learning project for Python automation,
AI testing and AI evaluation.

## What I will build

- A small application using fictional benefits scenarios
- Automated tests for inputs, APIs and data
- Checks for AI answers, citations and tool behavior
- Evaluation and regression reports

## Project data

This project uses synthetic examples and public sources.


---

# PolicyGuard — AI Agent Evaluation Confidence Lab

An independent Python/Pytest research and engineering project
for auditing the quality of AI-agent test evaluators.

## The Problem

AI-agent evaluations can report success even when important
failures go undetected.

For example, a tool might report that an inventory reservation
succeeded without actually changing the inventory.

An evaluator that checks only the success response may incorrectly
accept the operation.

PolicyGuard investigates how different evaluation strategies
detect known defects in controlled, stateful workflows.

## What PolicyGuard Does

The current prototype:

- Simulates a fictional inventory system.
- Introduces deliberately faulty implementations.
- Evaluates reported success and underlying system state.
- Checks for specifically prohibited action labels.
- Demonstrates overly strict evaluation of valid action sequences.
- Calculates fault-detection metrics.
- Generates reproducible JSON reports.
- Runs automated regression tests using Pytest.

## Evaluation Strategies

1. Response-only evaluation:
   Checks whether the operation reports success.

2. State-aware evaluation:
   Checks whether the expected inventory state was produced.

3. Combined evaluation:
   Checks response, final state, and prohibited action labels.

## Current Experiment

Four deliberately faulty inventory implementations are evaluated.

| Evaluator | Faults detected | Detection rate |
|---|---:|---:|
| Response-only | 0/4 | 0% |
| State-aware | 3/4 | 75% |
| Combined | 4/4 | 100% |

These results apply only to the four hand-designed synthetic
faults. They do not measure performance on real LLM agents.

## Technologies

- Python
- Pytest
- JSON
- Git and GitHub
- GitHub Actions

## Getting Started

Clone the repository:

```bash
git clone https://github.com/saisnehap/policyguard-ai-quality-lab.git
cd policyguard-ai-quality-lab
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Pytest:

```bash
python -m pip install pytest
```

Run automated tests:

```bash
python -m pytest -q
```

Run the fault-detection experiment:

```bash
python run_experiment.py
```

Generate the structured report:

```bash
python generate_report.py
```

Output:

`reports/evaluation_report.json`

## Project Architecture

- `policyguard/inventory.py` — Correct inventory simulator
- `policyguard/faulty_inventory.py` — Injected fault implementations
- `policyguard/evaluators.py` — Evaluation strategies
- `policyguard/metrics.py` — Fault-detection metrics
- `tests/` — Automated Pytest checks
- `run_experiment.py` — Initial evaluator comparison
- `generate_report.py` — Structured evaluation report
- `.github/workflows/` — CI configuration

## Research Direction

The long-term goal is to audit the effectiveness of AI-agent
test oracles through controlled fault injection.

Planned work includes:

- Structured agent action traces
- More diverse synthetic workflows
- Independent validity labels
- Measurement of false positives and false negatives
- Real LLM tool-calling experiments
- Comparisons with existing evaluation approaches

## Limitations

This version uses deterministic synthetic inventory scenarios,
not real model-generated agent behavior.

The fault set is small and manually selected.

Action validation currently uses simplified action labels.

The current experiments do not establish general superiority
over existing AI-agent evaluation frameworks.

## Independence and Data Privacy

This is an independent personal educational and research project.

It uses fictional data and publicly available technologies.
It does not use proprietary employer data, source code,
internal processes, or confidential information.
```

**Why this matters:** Research and engineering projects must be reproducible. A recruiter or engineer should be able to read the README and understand your design without needing you to explain everything first.

## 2. Save and test your project

Run:

```bash
python -m pytest -q
```

Then:

```bash
python generate_report.py
```

Expected: 40 tests passing and the evaluation report created successfully.

## 3. Commit the updated README

Run these commands one at a time:

```bash
git add README.md
```

```bash
git commit -m "Document PolicyGuard architecture and evaluation methodology"
```

```bash
git push origin main
```

## 4. Check your GitHub repository

Open <Link url="https://github.com/saisnehap/policyguard-ai-quality-lab">PolicyGuard on GitHub</Link> while signed into your account.

Confirm that your README displays the project description, evaluation results, setup instructions, and limitations.

Also check the Actions tab for the latest CI run.

## What you should learn from Step 13

When an interviewer asks, *"Tell me about your AI project,"* you should understand this answer:

> PolicyGuard is an experimental AI evaluation quality framework. I built a synthetic inventory simulator and deliberately introduced several defects. Then I compared evaluators that check only the response, the final state, or both the state and action constraints. My goal is to understand how test design influences the ability to detect unsafe or incorrect agent behavior.

This is accurate for the work you've completed.

---

{@body const [result,setResult]=DIL.useState("")}
<box border radius="xl" padding={3} gap={3}>
  **Step 13 — Submit your results**

  <textarea value={result} onChange={setResult} rows={5} placeholder="Paste your test results, git push result, README confirmation, and GitHub Actions status."/>
  <button block disabled={!result.trim()} onClick={()=>GenUI.issueNewTurn("PolicyGuard Step 13 results:\n\n"+result+"\n\nPlease verify my README, Git commit, and CI status. Give me only Step 14 to finish and release the MVP.")}>
    Verify Step 13 and proceed to final release <icon name="arrow-right" inline/>
  </button>
</box>

**After Step 13, only Step 14 remains for the initial MVP release.** We'll verify the repository, create a tagged version, and decide exactly what you can confidently claim on your resume and LinkedIn.