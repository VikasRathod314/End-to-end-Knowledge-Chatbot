import os

# Define the folder and file structure
folders = [
    "app/models",
    "app/services",
    "app/static",
    "app/templates"
]

files = [
    "requirements.txt",
    "app/__init__.py",
    "app/config.py",
    "app/main.py",
    "app/models/__init__.py",
    "app/models/vector_store.py",
    "app/services/__init__.py",
    "app/services/llm_service.py",
    "app/services/storage_service.py",
    "app/static/style.css",
    "app/templates/index.html"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file in files:
    with open(file, 'w') as f:
        pass  # Creates an empty file

print("✅ Project structure created successfully.")
