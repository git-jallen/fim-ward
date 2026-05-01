from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QFrame
)
from PySide6.QtCore import Qt

from .widgets import LogPanel, StatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ward")
        self.setMinimumSize(750, 550)

        self.controller = None
        self.directory = None

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(16)
        central.setLayout(main_layout)

        # Header
        self.title = QLabel("Ward")
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignCenter)

        self.subtitle = QLabel("File Integrity Monitoring Dashboard")
        self.subtitle.setObjectName("subtitle")
        self.subtitle.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(self.title)
        main_layout.addWidget(self.subtitle)

        # Directory card
        dir_card = QFrame()
        dir_card.setObjectName("sectionCard")
        dir_layout_outer = QVBoxLayout()
        dir_layout_outer.setSpacing(10)
        dir_card.setLayout(dir_layout_outer)

        dir_heading = QLabel("Monitored Directory")
        dir_heading.setStyleSheet("font-size: 16px; font-weight: 600; color: #7CFFB2;")
        dir_layout_outer.addWidget(dir_heading)

        dir_row = QHBoxLayout()
        dir_row.setSpacing(10)

        self.dir_label = QLabel("No directory selected")
        self.dir_label.setObjectName("dirLabel")

        self.browse_btn = QPushButton("Browse")
        self.browse_btn.setObjectName("browseButton")
        self.browse_btn.clicked.connect(self.select_directory)

        dir_row.addWidget(self.dir_label, 1)
        dir_row.addWidget(self.browse_btn)

        dir_layout_outer.addLayout(dir_row)
        main_layout.addWidget(dir_card)

        # Controls card
        controls_card = QFrame()
        controls_card.setObjectName("sectionCard")
        controls_layout = QVBoxLayout()
        controls_layout.setSpacing(10)
        controls_card.setLayout(controls_layout)

        controls_heading = QLabel("Controls")
        controls_heading.setStyleSheet("font-size: 16px; font-weight: 600; color: #7CFFB2;")
        controls_layout.addWidget(controls_heading)

        button_row = QHBoxLayout()
        button_row.setSpacing(10)

        self.baseline_btn = QPushButton("Create Baseline")
        self.baseline_btn.setObjectName("createBaselineButton")

        self.start_btn = QPushButton("Start Monitoring")
        self.start_btn.setObjectName("startButton")

        self.stop_btn = QPushButton("Stop Monitoring")
        self.stop_btn.setObjectName("stopButton")

        button_row.addWidget(self.baseline_btn)
        button_row.addWidget(self.start_btn)
        button_row.addWidget(self.stop_btn)

        controls_layout.addLayout(button_row)
        main_layout.addWidget(controls_card)

        # Log card
        log_card = QFrame()
        log_card.setObjectName("sectionCard")
        log_layout = QVBoxLayout()
        log_layout.setSpacing(10)
        log_card.setLayout(log_layout)

        log_heading = QLabel("Event Log")
        log_heading.setStyleSheet("font-size: 16px; font-weight: 600; color: #7CFFB2;")
        log_layout.addWidget(log_heading)

        self.log_panel = LogPanel()
        log_layout.addWidget(self.log_panel)

        main_layout.addWidget(log_card, 1)

        # Status
        self.status = StatusBar()
        main_layout.addWidget(self.status)

    def set_controller(self, controller):
        self.controller = controller

    def select_directory(self):
        dialog = QFileDialog(self, "Select Directory")
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)

        if dialog.exec():
            selected = dialog.selectedFiles()
            if selected:
                folder = selected[0]
                self.directory = folder
                self.dir_label.setText(folder)

                if self.controller:
                    self.controller.set_directory(folder)

                self.log_panel.add_log(f"[INFO] Selected directory: {folder}")

    def log(self, message):
        self.log_panel.add_log(message)

    def set_status(self, text):
        self.status.set_status(text)

    def set_files_monitored(self, count):
        self.log_panel.add_log(f"[INFO] Files in baseline: {count}")