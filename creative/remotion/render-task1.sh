#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
npx remotion render src/index.ts Task1Reel ../demo-v1.mp4 --props=data/task1.json --codec=h264 --crf=18 --concurrency=4
