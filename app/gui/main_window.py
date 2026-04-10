from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog
)
from PySide6.QtCore import Qt

from .widgets import LogPanel, StatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ward")
        self.setMinimumSize(800, 500)

        self.directory = None

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # ===== HEADER =====
        self.title = QLabel("🛡️ Ward")
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)

        # ===== DIRECTORY SELECT =====
        dir_layout = QHBoxLayout()

        self.dir_label = QLabel("No directory selected")
        self.dir_label.setObjectName("dirLabel")

        self.browse_btn = QPushButton("Browse")
        self.browse_btn.clicked.connect(self.select_directory)

        dir_layout.addWidget(self.dir_label)
        dir_layout.addWidget(self.browse_btn)

        self.layout.addLayout(dir_layout)

        # ===== CONTROL BUTTONS =====
        btn_layout = QHBoxLayout()

        self.baseline_btn = QPushButton("Create Baseline")
        self.start_btn = QPushButton("Start Monitoring")
        self.stop_btn = QPushButton("Stop Monitoring")

        btn_layout.addWidget(self.baseline_btn)
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)

        self.layout.addLayout(btn_layout)

        # ===== LOG PANEL =====
        self.log_panel = LogPanel()
        self.layout.addWidget(self.log_panel)

        # ===== STATUS BAR =====
        self.status = StatusBar()
        self.layout.addWidget(self.status)

    # ===== UI EVENTS ======

    def select_directory(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder:
            self.directory = folder
            self.dir_label.setText(folder)
            self.log_panel.add_log(f"[INFO] Selected directory: {folder}")

    # conenct to controller later
    def log(self, message):
        self.log_panel.add_log(message)

    def set_status(self, text):
        self.status.set_status(text)

    def set_controller(self, controller):
        self.controller = controller

    # override directory selection
        self.browse_btn.clicked.disconnect()
        self.browse_btn.clicked.connect(self._select_directory)

    def _select_directory(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder:
            self.directory = folder
            self.dir_label.setText(folder)

            # Tell controller
            self.controller.set_directory(folder)

            self.log_panel.add_log(f"[INFO] Selected directory: {folder}")