# GitHub Actions — Hands-on Practical Kit

This kit follows the uploaded **Practical - Github Actions** presentation: create a repository, add a workflow YAML under `.github/workflows/`, commit it, open Actions, inspect the run, then change code and commit again to trigger CI.

## What learners will build
A small Python project whose GitHub Actions workflow runs automatically on pushes and pull requests.

## Contents
- `01_PREREQUISITES_AND_REPOSITORY.md` — account/repository setup
- `02_WORKFLOW_EXPLAINED.md` — YAML explained line by line
- `03_PRACTICAL_STEPS.md` — complete click-by-click lab
- `04_TRAINER_SCRIPT.md` — teaching notes and timing
- `05_LEARNER_WORKSHEET.md` — learner tasks and evidence
- `06_TROUBLESHOOTING.md` — common failures
- `07_VIVA_QUESTIONS.md` — questions with answers
- `08_CLEANUP_AND_NEXT_STEPS.md` — cleanup and extensions
- `.github/workflows/ci.yml` — ready-to-use workflow
- `app/main.py` — sample Python program
- `app/test_main.py` — simple unit tests
- `requirements.txt` — test dependency

## Quick start
1. Create a GitHub repository named `github-actions-practical`.
2. Upload all files from this folder to the repository, preserving the `.github/workflows/` path.
3. Commit to the `main` branch.
4. Open the **Actions** tab and inspect the workflow run.
5. Edit `app/main.py`, commit again, and verify that a new run starts.

The workflow uses GitHub-hosted runners. No AWS account or secret is required for this introductory lab.
