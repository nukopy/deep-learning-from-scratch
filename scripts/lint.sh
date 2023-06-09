#!/usr/bin/env bash

set -ex

mypy app
ruff app tests
