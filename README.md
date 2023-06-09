# template-python-app

![GitHub Actions workflow badge](https://github.com/nukopy/template-python-app/actions/workflows/ci.yml/badge.svg?branch=main)

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
