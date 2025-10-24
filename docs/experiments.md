# Experiments Playbook

This document walks through the three required merge experiments. Adapt the commands to match each collaborator's workspace.

## Shared Setup
- Protect `main` on GitHub: require PR, passing GitHub Actions, block direct pushes, allow merge commit / squash / rebase.
- Each collaborator clones the repository separately (or uses `git worktree`) so conflicts come from concurrent commits.
- Always sync from `origin/main` before starting a new experiment branch.

## Experiment 1 – Same File, Same Lines
1. Developer A: `git checkout -b exp1-a`, modify the same line that Developer B will edit, commit, push, open PR.
2. Developer B: `git checkout -b exp1-b`, make a conflicting edit on *the identical lines*, push, open PR.
3. Merge A's PR first using **Merge commit**. B's PR will go red with conflicts.
4. B pulls `main`, resolves conflicts locally, pushes the resolution commit.
5. After CI passes, merge B's PR using **Squash & merge** so the resolution is a single commit.
6. Capture screenshots of the conflict, the CI run, and the resulting `git log --graph`.

## Experiment 2 – Same File, Different Lines
1. A: `git checkout -b exp2-a`, edit section X of the target file.
2. B: `git checkout -b exp2-b`, edit section Y (non-overlapping) of the same file.
3. Merge A's PR using **Rebase & merge** to keep the history linear.
4. B rebases onto new `main` if needed; conflicts should be trivial or none.
5. Merge B's PR (merge style optional) once CI is green; document the clean merge result.

## Experiment 3 – Different Files
1. A: `git checkout -b exp3-a`, create or modify `docs/` content.
2. B: `git checkout -b exp3-b`, change code under `app/`.
3. Merge one PR via **Squash**, the other via a **fast-forward** (can be done locally then pushed).
4. Note how CI runs in parallel and how fast merges unblock the queue.

## Evidence Collection Checklist
- PR URLs and chosen merge styles
- Screenshots of GitHub Actions (blocked & successful)
- Conflict description + final resolved snippet
- `git log --graph --oneline --decorate` output per experiment
- Observations on CI timing and merge policy implications

## Stretch Goals
- Enable matrix builds (e.g., Python 3.9–3.11) in CI.
- Try `git rerere` or `git range-diff` to streamline conflict handling.
- Draft policy recommendations comparing merge strategies (auditability, revert ease).
