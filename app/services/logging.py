import os
import json
from datetime import datetime

LOG_PATH = "data/logs/fim.log"


def log_event(event_type, file_path, metadata=None):
    """
    Writes structured security event logs.
    """

    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "file": file_path,
        "metadata": metadata or {}
    }

    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(event) + "\n")


def read_logs(limit=50):
    """
    Reads last N logs for UI or analysis.
    """

    if not os.path.exists(LOG_PATH):
        return []

    with open(LOG_PATH, "r") as f:
        lines = f.readlines()

    return [json.loads(line) for line in lines[-limit:]]