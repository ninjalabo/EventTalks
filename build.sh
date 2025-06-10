#!/usr/bin/env bash
set -euo pipefail                              # fail fast on any error

echo "▶ nbdev_prepare"
nbdev_prepare

echo "▶ nbdev_export"
nbdev_export

echo "▶ nbdev_test"
nbdev_test                                     # run your unit tests

echo "▶ docker compose build"
docker compose build --no-cache              # rebuild images from scratch

echo "▶ docker compose up  (foreground)"
docker compose up                             # Ctrl-C to stop
