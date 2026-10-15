# 03 — Practical: Create, run, inspect and retrigger CI

## Part A — Add the project
1. Open your `github-actions-practical` repository.
2. Upload `app/main.py`, `app/test_main.py`, `requirements.txt`, and `.github/workflows/ci.yml` from this kit. Preserve the folder paths.
3. Commit the files to `main` with message `Add Python CI workflow`.

## Part B — Open Actions
1. Open the repository's **Actions** tab.
2. Select **Python CI** if it appears in the left panel.
3. Open the newest run.
4. Open the `test` job.
5. Expand each step and read its logs.
6. Confirm the test and application steps completed successfully.

## Part C — Trigger CI again
1. Open `app/main.py` in the repository.
2. Select the edit/pencil control.
3. Change the greeting text, for example from `Hello from GitHub Actions!` to `Hello again from automated CI!`.
4. Commit the change to `main`.
5. Return to **Actions** and confirm a new run starts automatically.

## Part D — Optional failure demonstration
Temporarily change the expected result in `app/test_main.py` so it does not match the application output. Commit the change and observe the test step fail. Restore the correct expected value and commit again. Confirm the next run passes.

## Success criteria
- Workflow appears in Actions.
- Workflow triggers after a commit to `main`.
- Checkout, Python setup, dependency installation, tests and application steps run.
- Learner can locate the logs and explain a failed step.
