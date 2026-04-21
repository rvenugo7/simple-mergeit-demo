# Simple MergeIt Demo Repo

This repository is intentionally small and is meant only for testing MergeIt.

It contains one simple Python module and a small test suite. Two feature
branches make different changes to the same function so that merging them
creates a straightforward conflict.

## Files

- `app/pricing.py`
- `tests/test_pricing.py`

## How Graders Can Reproduce The Conflict

After cloning this repository:

```bash
git checkout feature/add-student-discount
git checkout -b demo/conflict-test
git merge feature/add-tax-rounding
```

That merge should create conflicts in:

- `app/pricing.py`
- `tests/test_pricing.py`

## Expected Intent Of Each Branch

- `feature/add-student-discount`
  - add a student discount before returning the final price
- `feature/add-tax-rounding`
  - apply tax and round the final price to two decimals

The correct merge should preserve both behaviors.
