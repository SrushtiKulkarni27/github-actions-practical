# 06 — Troubleshooting

## Workflow does not appear in Actions
- Confirm file path is `.github/workflows/ci.yml`.
- Confirm the file is committed to the repository.
- Check YAML indentation and syntax.
- Check repository Actions settings/policies.

## Workflow does not trigger
- Confirm the commit was pushed to `main`.
- Check the `on.push.branches` setting.
- Make sure the workflow file is present on the branch receiving the event.

## YAML syntax error
- Use spaces rather than tabs.
- Check each nested section's indentation.
- Ensure strings with special characters are quoted where needed.

## Dependency installation fails
- Confirm `requirements.txt` exists at repository root.
- Check package name/version and the install log.

## Unit test fails
- Expand the test step in the job logs.
- Compare the expected value with the function's actual output.
- Fix the code or test intentionally, then commit again.

## Permission or policy issue
- Check repository Settings → Actions policies.
- This sample only needs `contents: read`; it does not need write permissions or secrets.
