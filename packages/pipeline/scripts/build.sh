#!/bin/bash
# Build script for Python package

echo "Building Python package..."

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Run 'pnpm setup' first."
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

# Install in editable mode (no wheel needed for now)
pip install -e .

echo "✅ Build complete!"