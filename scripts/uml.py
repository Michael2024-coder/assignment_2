# scripts/uml.py
import os
import subprocess
import sys
import shutil

# Paths
SOURCE_DIR = "dice"  # replace with your actual package folder
OUTPUT_DIR = os.path.join("doc", "uml")
PROJECT_NAME = "uml"

# Check if Graphviz is installed
if shutil.which("dot") is None:
    print("✗ Graphviz not found. Please install Graphviz and make sure 'dot' is on your PATH.")
    print("   Download: https://graphviz.org/download/")
    sys.exit(1)

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Run pyreverse
result = subprocess.run(
    ["pyreverse", "-o", "png", "-p", PROJECT_NAME, SOURCE_DIR, "-d", OUTPUT_DIR],
    capture_output=True,
    text=True,
)

# Check result
if result.returncode == 0:
    print(f"✓ UML diagrams saved to {OUTPUT_DIR}")
else:
    print("✗ UML generation failed")
    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)
    sys.exit(result.returncode)
