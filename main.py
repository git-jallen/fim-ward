import sys
from PySide6.QtWidgets import QApplication

from app.gui.main_window import MainWindow
from app.controller.fim_controller import FIMController


def load_styles(app):
    with open("app/gui/styles.qss", "r") as f:
        app.setStyleSheet(f.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    load_styles(app)

    # Create GUI
    window = MainWindow()

    # Create Controller and connect it
    controller = FIMController(window)
    window.set_controller(controller)

    window.show()

    sys.exit(app.exec())