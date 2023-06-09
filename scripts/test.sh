#!/usr/bin/env bash

set -ex
pytest -v tests --cov=app --junitxml=reports/junit/test-results.xml --cov-report=xml --cov-report=html
