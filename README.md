# deep-learning-from-scratch

![GitHub Actions workflow badge](https://github.com/nukopy/deep-learning-from-scratch/actions/workflows/ci.yml/badge.svg?branch=main)

## Requirements

- Python 3.11
- Poetry

## Setup

- Setup direnv

```sh
echo "source .venv/bin/activate" >> .envrc
direnv allow
```

- Install dependencies

```sh
poetry install
```

- Run tests

```sh
bash scripts/test.sh
```
