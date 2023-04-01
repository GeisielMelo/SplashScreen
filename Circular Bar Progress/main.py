# import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QSlider,
                               QVBoxLayout)

from widgets import CircularProgress

# from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Resize Window
        self.resize(500, 500)

        # Remove Title bar
        self.setWindowFlags(Qt.FramelessWindowHint)  # type: ignore
        self.setAttribute(Qt.WA_TranslucentBackground)  # type: ignore

        # Create container and layout
        self.container = QFrame()
        self.container.setStyleSheet("background-color: transparent")
        self.layout = QVBoxLayout()  # type: ignore

        # Create Circular Progress
        self.progress = CircularProgress()
        self.progress.value = 0
        self.progress.suffix = "%"
        self.progress.font_size = 12
        self.progress.setMinimumSize(
            self.progress.width, self.progress.height)  # type: ignore
        self.progress.addShadow(True)

        # Add Slider
        self.slider = QSlider(Qt.Horizontal)  # type: ignore
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.change_value)

        # Add Widgets
        self.layout.addWidget(
            self.progress, Qt.AlignCenter, Qt.AlignCenter  # type: ignore
            )
        self.layout.addWidget(
            self.slider, Qt.AlignCenter, Qt.AlignCenter  # type: ignore
            )

        # Set center Widget
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # Show Window
        self.show()

    def change_value(self, value):
        self.progress.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
