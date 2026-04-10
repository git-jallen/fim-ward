from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class FileRecord:
    """
    Represents a file in the FIM system.

    Can be used for:
    - Baseline entries
    - Change detection events
    """

    path: str
    file_hash: Optional[str] = None
    event_type: Optional[str] = None  # NEW, MODIFIED, DELETED
    timestamp: str = datetime.utcnow().isoformat()

    def is_event(self) -> bool:
        """
        Returns True if this record represents a security event.
        """
        return self.event_type is not None

    def to_dict(self) -> dict:
        """
        Convert to dictionary (for logging / JSON storage).
        """
        return {
            "path": self.path,
            "file_hash": self.file_hash,
            "event_type": self.event_type,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Reconstruct FileRecord from dictionary.
        """
        return FileRecord(
            path=data.get("path"),
            file_hash=data.get("file_hash"),
            event_type=data.get("event_type"),
            timestamp=data.get("timestamp", datetime.utcnow().isoformat())
        )