import os

# Directory structure
dirs = [
    ".github/workflows",
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "src/data",
    "src/models",
    "src/evaluation",
    "src/utils",
    "tests"
]

# Files to create
files = [
    ".github/workflows/ci.yml",
    "src/__init__.py",
    "src/data/__init__.py",
    "src/data/load_data.py",
    "src/data/preprocess.py",
    "src/models/__init__.py",
    "src/models/train.py",
    "src/models/predict.py",
    "src/evaluation/__init__.py",
    "src/evaluation/evaluate.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "tests/test_data.py",
    "tests/test_models.py",
    "tests/test_utils.py",
    ".gitignore",
    "README.md",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "requirements.txt"
]

# Create directories
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# Create files with empty content
for file in files:
    with open(file, 'w') as f:
        pass

print("Project structure created successfully.")

