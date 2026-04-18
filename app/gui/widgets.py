from PySide6.QtWidgets import QTextEdit, QLabel, QHBoxLayout, QWidget
from PySide6.QtCore import Qt


class LogPanel(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setObjectName("logPanel")

    def add_log(self, message):
        if "MODIFIED" in message:
            color = "#ffbf66"
        elif "DELETED" in message:
            color = "#ff8f9b"
        elif "NEW" in message:
            color = "#7CFFB2"
        elif "ERROR" in message:
            color = "#ff6b6b"
        elif "INFO" in message:
            color = "#59c3ff"
        else:
            color = "#e8ecf1"

        self.append(f"<span style='color:{color};'>{message}</span>")


class StatusBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("statusContainer")

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 6, 10, 6)
        self.setLayout(layout)

        self.label = QLabel("Status: Idle")
        self.label.setAlignment(Qt.AlignLeft)
        self.label.setObjectName("statusLabel")

        layout.addWidget(self.label)

    def set_status(self, text):
        self.label.setText(f"Status: {text}")