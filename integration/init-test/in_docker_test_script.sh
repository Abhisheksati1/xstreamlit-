#!/usr/bin/env bash

set -ex

echo "Preparing test project dir"
mkdir hello
python3 -m venv ~/hello/venv
source ~/hello/venv/bin/activate

echo "Installing dotserve from local repo code"
cd /dotserve-repo
poetry install
echo "Running dotserve init in test project dir"
export TELEMETRY_ENABLED=false
poetry run /bin/bash -c "cd ~/hello && dotserve init && rm -rf ~/.dotserve .web && dotserve export --backend-only"