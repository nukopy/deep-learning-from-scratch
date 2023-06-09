#!/usr/bin/env bash

set -ex

ruff app tests --fix
black app tests
