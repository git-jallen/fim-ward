import json
import os

CONFIG_PATH = "data/config.json"

DEFAULT_CONFIG = {
    "scan_interval": 3,
    "hash_algorithm": "sha256",
    "monitored_directories": [],
    "enable_logging": True
}


def load_config():
    """
    Loads config or creates default if not found.
    """

    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def save_config(config):
    """
    Saves config to disk.
    """

    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)


def update_config(key, value):
    """
    Updates a single config value safely.
    """

    config = load_config()
    config[key] = value
    save_config(config)
    return config