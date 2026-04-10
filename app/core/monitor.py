import os
import time
from ..services.hashing import hash_file


class FileSystemMonitor:
    """
    Responsible for scanning directories and returning file states.
    This is a PURE data collector (no detection logic here).
    """

    def __init__(self, directory, scan_interval=3):
        self.directory = directory
        self.scan_interval = scan_interval

    def scan(self):
        """
        Returns current snapshot of file system:
        { file_path: file_hash }
        """

        state = {}

        for root, _, files in os.walk(self.directory):
            for file in files:
                path = os.path.join(root, file)
                file_hash = hash_file(path)

                if file_hash:
                    state[path] = file_hash

        return state

    def stream_scans(self):
        """
        Generator that yields filesystem snapshots over time.
        Useful for continuous monitoring loops.
        """

        while True:
            yield self.scan()
            time.sleep(self.scan_interval)