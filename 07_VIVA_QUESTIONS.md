# 07 — Viva questions and short answers

1. **What is GitHub Actions?** A GitHub automation platform for workflows such as CI and CD.
2. **What is a workflow?** An automated process defined in a YAML file.
3. **Where are workflow files stored?** In `.github/workflows/`.
4. **What is a trigger?** An event that starts a workflow.
5. **What is a runner?** A machine that executes workflow jobs.
6. **What does checkout do?** Retrieves repository files into the runner workspace.
7. **What is a job?** A set of steps executed on a runner.
8. **What is a step?** An action or command within a job.
9. **What is CI?** Automatically building and testing code changes to find issues early.
10. **How do you inspect a failed run?** Open Actions, select the run and job, then inspect the failed step logs.
11. **Why use unit tests?** To check expected program behavior automatically.
12. **Should secrets be hard-coded in YAML?** No; use an appropriate secret store only when a workflow truly needs credentials.
13. **What event starts this workflow after a commit?** A `push` to `main`.
14. **What is the purpose of `permissions: contents: read`?** It limits repository content permission to read access for this workflow.
15. **Does this lab require AWS credentials?** No.
