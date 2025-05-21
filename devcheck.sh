#!/usr/bin/env bash
set -euo pipefail           # stop on first error, undefined var, or pipe fail

echo "🔄  nbdev_export ..."
nbdev_export

echo "🧹  nbdev_clean ..."
nbdev_clean

echo "▶️  nbdev_test ..."
nbdev_test

echo "🔍  Ruff lint ..."
ruff check . --fix
ruff check .

echo "🎨  Black formatting ..."
black --check .

echo "📦  Build wheel / sdist ..."
python -m build

echo "✅  devcheck finished successfully!"
