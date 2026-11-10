# Metra Lint

Schema linter for the lab's measurement pipelines.

## Release status

Released: v1.4.2 is publicly available from this repository.

## Usage

```
python -m metra_lint --schema data/schema_rules.yaml --input runs/
```

## Layout

- `src/metra_lint.py` — validator implementation
- `data/schema_rules.yaml` — shipped rule set
- `experiments/lint_benchmark.md` — nightly benchmark notes
