class ChangeDetector:
    """
    Compares filesystem snapshots and generates events.
    """

    def __init__(self):
        self.previous_state = None

    def analyze(self, current_state):
        """
        Compares current state to previous state.
        Returns list of security events.
        """

        if self.previous_state is None:
            self.previous_state = current_state
            return []

        events = []

        old_files = set(self.previous_state.keys())
        new_files = set(current_state.keys())

        # Detect deleted files
        for path in old_files - new_files:
            events.append({
                "type": "DELETED",
                "file": path
            })

        # Detect new files
        for path in new_files - old_files:
            events.append({
                "type": "NEW",
                "file": path
            })

        # Detect modified files
        for path in old_files & new_files:
            if self.previous_state[path] != current_state[path]:
                events.append({
                    "type": "MODIFIED",
                    "file": path
                })

        # Update state
        self.previous_state = current_state

        return events