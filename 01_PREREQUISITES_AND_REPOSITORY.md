# 01 — Prerequisites and repository setup

## Before starting
- GitHub account with permission to create a repository
- Web browser and internet access
- Basic understanding of files, folders, Python and YAML
- No AWS account is needed for this lab

## Create the repository
1. Sign in to GitHub.
2. Select **New repository**.
3. Repository name: `github-actions-practical`.
4. Choose **Public** for a simple classroom lab, or **Private** if preferred.
5. Add a README if creating the repository manually; alternatively upload the supplied files into an empty repository.
6. Create the repository.

## Important folder path
The workflow file must be saved at this exact path:

```text
.github/workflows/ci.yml
```

GitHub Actions discovers workflow YAML files inside `.github/workflows/`. A file named `ci.yml` elsewhere in the repository will not run as a workflow.
