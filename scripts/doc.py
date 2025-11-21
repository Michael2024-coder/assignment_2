# scripts/doc.py
import os
import subprocess
import sys

# Paths
SOURCE_DIR = os.path.join("doc", "api")
BUILD_DIR = os.path.join(SOURCE_DIR, "html")

# Ensure build directory exists
os.makedirs(BUILD_DIR, exist_ok=True)

# Run Sphinx
result = subprocess.run(
    [sys.executable, "-m", "sphinx", "-b", "html", SOURCE_DIR, BUILD_DIR],
    capture_output=True,
    text=True
)

# Check result
if result.returncode == 0:
    print(f"✓ Documentation built at {BUILD_DIR}")
else:
    print("✗ Docs generation failed")
    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)
    sys.exit(result.returncode)
