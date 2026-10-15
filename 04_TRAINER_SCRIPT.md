# 04 — Trainer script (45–60 minutes)

## 1. Introduction (5 min)
Say: “GitHub stores our code. GitHub Actions automatically runs tasks when an event, such as a commit, occurs. Today we will automate a simple Python test.”

Draw:

```text
Developer commits code → GitHub repository → Workflow trigger
                                           ↓
                                Hosted Ubuntu runner
                                           ↓
                           Checkout → Setup Python → Test
                                           ↓
                                      Pass / Fail
```

## 2. Explain repository layout (5 min)
Show `.github/workflows/ci.yml`, `app/main.py`, `app/test_main.py` and `requirements.txt`. Emphasize that the workflow path is important.

## 3. Add and commit files (10 min)
Ask learners to upload files while preserving folders, then commit to `main`.

## 4. Inspect the run (10 min)
Open Actions → Python CI → latest run → `test`. Explain each step and how logs help troubleshoot.

## 5. Trigger again (5–10 min)
Edit the greeting, commit, and watch the new run. Connect the commit event to the `on.push` rule.

## 6. Failure demonstration (10 min)
Introduce an intentional test mismatch. Show the failed step and log output. Fix the expected value and commit again.

## 7. Recap (5 min)
Ask: What triggers the workflow? What is a runner? Why is the workflow in `.github/workflows/`? Where do you inspect logs?

## Trainer caution
Do not put passwords, tokens or cloud access keys in workflow YAML or repository files. This introductory workflow needs no secrets.
