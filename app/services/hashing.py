import hashlib


def hash_file(filepath, algorithm="sha256"):
    """
    Generate a hash for a file.
    Default: SHA-256 (industry standard for integrity checking)
    """

    try:
        hasher = hashlib.new(algorithm)

        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)

        return hasher.hexdigest()

    except (FileNotFoundError, PermissionError, OSError):
        return None