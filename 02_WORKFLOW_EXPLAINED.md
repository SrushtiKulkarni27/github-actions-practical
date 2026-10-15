# 02 — Workflow YAML explained

The ready-to-use workflow is `.github/workflows/ci.yml`.

```yaml
name: Python CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: python -m pip install -r requirements.txt

      - name: Run unit tests
        run: python -m unittest discover -s app -p 'test_*.py' -v

      - name: Run application
        run: python app/main.py
```

## Line-by-line
- `name`: friendly workflow name shown in Actions.
- `on`: events that start the workflow. Here, pushes and pull requests targeting `main`.
- `permissions`: gives the workflow read-only access to repository contents, which is sufficient for this lab.
- `jobs`: groups the work the runner must perform.
- `test`: this job's identifier.
- `runs-on`: selects a GitHub-hosted Ubuntu runner.
- `steps`: commands and reusable actions executed in sequence.
- `actions/checkout`: downloads the repository files into the runner workspace.
- `actions/setup-python`: configures Python on the runner.
- `run`: executes a shell command.

## YAML reminders
- Use spaces, not tabs, for indentation.
- Keep indentation consistent.
- Quote values such as `'3.x'` for clarity.
- Workflow file extension should be `.yml` or `.yaml`.
