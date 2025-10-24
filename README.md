# CI Merge Experiments Lab

This repository scaffolds the exercises for exploring merge strategies under Continuous Integration gates.

## Overview
- Sample Python package with unit tests for demonstrating CI checks
- GitHub Actions workflow template ready for lint and test stages
- Suggested branch naming and workflow guidance stored in `docs/`

## Quick Start
1. Fork or clone this repo into your GitHub account.
2. Add collaborators and configure branch protections on `main` (require PR reviews + passing CI).
3. Each teammate works from their own clone or `git worktree` to simulate parallel development.

## Local Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Next Steps
- Use `docs/experiments.md` for instructions on running the three merge experiments.
- Update `.github/workflows/build-test-release.yml` to match your project tooling if needed.
- Record PR links, CI screenshots, and git history graphs for the final report.
