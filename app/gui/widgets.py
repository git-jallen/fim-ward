from PySide6.QtWidgets import QTextEdit, QLabel, QHBoxLayout, QWidget
from PySide6.QtCore import Qt


class LogPanel(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setObjectName("logPanel")

    def add_log(self, message):
        # Color coding
        if "MODIFIED" in message:
            color = "orange"
        elif "DELETED" in message:
            color = "red"
        elif "NEW" in message:
            color = "lightgreen"
        elif "INFO" in message:
            color = "#00bfff"
        else:
            color = "white"

        self.append(f"<span style='color:{color}'>{message}</span>")


class StatusBar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Status: Idle")
        self.label.setAlignment(Qt.AlignLeft)
        self.label.setObjectName("statusLabel")

        layout.addWidget(self.label)

    def set_status(self, text):
        self.label.setText(f"Status: {text}")