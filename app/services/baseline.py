import os
import json
from .hashing import hash_file

BASELINE_PATH = "data/baseline.json"


def create_baseline(directory):
    """
    Scans directory and creates a file integrity baseline.
    """

    baseline = {}

    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_hash = hash_file(path)

            if file_hash:
                baseline[path] = file_hash

    return baseline


def save_baseline(baseline, path=BASELINE_PATH):
    """
    Saves baseline to disk.
    """

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        json.dump(baseline, f, indent=4)


def load_baseline(path=BASELINE_PATH):
    """
    Loads baseline from disk.
    """

    try:
        with open(path, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return {}