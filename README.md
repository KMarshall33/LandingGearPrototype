# Landing Gear Control System – Functional Configuration Prototype

## Overview

This repository contains a **simulation-driven functional configuration prototype** for a **safety-critical landing gear control system**, developed in the context of an aerospace software engineering assignment.

The prototype demonstrates how analysed behaviour and an agreed baseline can be translated into a **controlled implementation** suitable for review, validation and improvement. It is not a production system and intentionally operates at an appropriate level of abstraction.

The system focuses on:

* Deterministic state behaviour
* Controlled component integration
* Simulation-based execution
* Quality assurance and structured problem-solving techniques

---

## Scope and Intent

The prototype models a simplified landing gear deployment sequence, including:

* Discrete gear states (e.g. up locked, transitioning, down locked)
* Command handling and state transitions
* Simulation-driven behaviour rather than instantaneous transitions
* Safety-oriented constraints and fault handling (added iteratively)

Out of scope:

* Real-time scheduling
* Continuous mechanical or hydraulic modelling
* Hardware interfaces
* Certification artefacts

These limitations are deliberate and reflect the goals of a functional prototype rather than a certified system.

---

## Repository Structure

```
.
├── landing_gear.py         # Core prototype implementation
├── tests/                  # Automated tests (pytest)
├── .github/
│   └── workflows/
│       └── ci.yml          # CI pipeline (automated test execution)
└── README.md
```

---

## Running the Prototype

To run the prototype locally:

```bash
python landing_gear.py
```

This will execute a simple demonstration of the landing gear control logic and log state transitions to the console.

---

## Automated Testing

Automated tests are implemented using **pytest** to validate:

* Correct state transitions
* Constraint handling
* Fault and abnormal behaviour
* Integration between controller logic and simulated components

To run tests locally:

```bash
pytest
```

---

## Continuous Integration

This repository uses **GitHub Actions** to automatically run the test suite on every push and pull request.

The CI pipeline provides:

* Repeatable verification of behaviour
* Early detection of integration errors
* Evidence of professional development practice suitable for safety-critical contexts

Successful pipeline runs form part of the validation evidence for the prototype.

---

## Quality Assurance Approach

Quality assurance is applied through:

* Automated testing and regression checks
* Structured logging of system behaviour
* Incremental development with version control
* Root cause analysis of observed issues and iterative improvement

These techniques are used to improve reliability, correctness and maintainability while reducing integration risk.

---

## Disclaimer

This software is a **learning and demonstration artefact** produced for academic purposes. It is not intended for operational use in real aircraft systems.

---
