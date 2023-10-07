#!/usr/bin/env bash

set -ex

echo "Preparing test project dir"
mkdir hello
python3 -m venv ~/hello/venv
source ~/hello/venv/bin/activate

echo "Installing dotreact from local repo code"
cd /dotreact-repo
poetry install
echo "Running dotreact init in test project dir"
export TELEMETRY_ENABLED=false
poetry run /bin/bash -c "cd ~/hello && dotreact init && rm -rf ~/.dotreact .web && dotreact export --backend-only"