#!/usr/bin/env bash

set -ex

mypy app tests
ruff app tests
black app tests --check
