# 08 — Cleanup and next steps

## Cleanup
No cloud resources are created by this lab. If the repository is only for practice, you may keep it as a portfolio example or delete it from GitHub repository Settings → General → Danger Zone. Deletion is permanent; confirm before proceeding.

## Extensions
1. Add linting.
2. Add a Go or Java test workflow.
3. Add a build artifact upload step.
4. Run the workflow on pull requests and require checks before merging.
5. Deploy to AWS only after learning GitHub Secrets/OIDC, IAM least privilege and environment protection.

Never store long-lived cloud keys in source code. Prefer short-lived credentials with AWS OIDC where suitable for a deployment lab.
