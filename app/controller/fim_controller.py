import os
import time
from PySide6.QtCore import QObject, QThread, Signal

from app.services.hashing import hash_file
from app.services.baseline import create_baseline, load_baseline, save_baseline
from app.services.logging import log_event
from app.core.monitor import FileSystemMonitor
from app.core.detector import ChangeDetector


# ============================
# MONITOR WORKER THREAD
# ============================
class MonitorWorker(QThread):
    event_signal = Signal(dict)

    def __init__(self, directory, interval=3):
        super().__init__()
        self.directory = directory
        self.interval = interval
        self.running = True

        self.monitor = FileSystemMonitor(directory, interval)
        self.detector = ChangeDetector()

    def run(self):
        for snapshot in self.monitor.stream_scans():
            if not self.running:
                break

            events = self.detector.analyze(snapshot)

            for event in events:
                self.event_signal.emit(event)

    def stop(self):
        self.running = False
        self.quit()
        self.wait()


# ============================
# MAIN CONTROLLER
# ============================
class FIMController(QObject):
    def __init__(self, gui):
        super().__init__()

        self.gui = gui
        self.directory = None
        self.baseline = {}
        self.worker = None
        self.is_running = False

        self._connect_ui()

    # ============================
    # CONNECT GUI EVENTS
    # ============================
    def _connect_ui(self):
        self.gui.baseline_btn.clicked.connect(self.create_baseline)
        self.gui.start_btn.clicked.connect(self.start_monitoring)
        self.gui.stop_btn.clicked.connect(self.stop_monitoring)

    # ============================
    # DIRECTORY HANDLING
    # ============================
    def set_directory(self, path):
        self.directory = path
        self.gui.set_status(f"Directory set: {path}")

    # ============================
    # BASELINE
    # ============================
    def create_baseline(self):
        if not self.directory:
            self.gui.log("[ERROR] No directory selected")
            return

        self.baseline = create_baseline(self.directory)
        save_baseline(self.baseline)

        self.gui.log("[INFO] Baseline created successfully")
        self.gui.set_status("Baseline Ready")

    # ============================
    # MONITORING CONTROL
    # ============================
    def start_monitoring(self):
        if not self.directory:
            self.gui.log("[ERROR] No directory selected")
            return

        self.worker = MonitorWorker(self.directory)
        self.worker.event_signal.connect(self.handle_event)
        self.worker.start()

        self.is_running = True
        self.gui.set_status("Monitoring Active")
        self.gui.log("[INFO] Monitoring started")

    def stop_monitoring(self):
        if self.worker:
            self.worker.stop()
            self.worker = None

        self.is_running = False
        self.gui.set_status("Stopped")
        self.gui.log("[INFO] Monitoring stopped")

    # ============================
    # EVENT HANDLER
    # ============================
    def handle_event(self, event):
        event_type = event["type"]
        file_path = event["file"]

        message = f"[{event_type}] {file_path}"

        # Send to GUI
        self.gui.log(message)

        # Persist log (future-proofing)
        log_event(event_type, file_path)

        # Status updates
        if event_type == "MODIFIED":
            self.gui.set_status("ALERT: File Modified")
        elif event_type == "DELETED":
            self.gui.set_status("ALERT: File Deleted")
        elif event_type == "NEW":
            self.gui.set_status("New File Detected")