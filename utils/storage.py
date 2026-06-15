import json
import os

DATA_DIR = "data"


def load_data(filename):
    path = os.path.join(DATA_DIR, filename)

    try:
        if not os.path.exists(path):
            return []

        with open(path, "r") as f:
            return json.load(f)

    except json.JSONDecodeError:
        return []


def save_data(filename, data):
    path = os.path.join(DATA_DIR, filename)

    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    except Exception as e:
        print(f"Error saving {filename}: {e}")