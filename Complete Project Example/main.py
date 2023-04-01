import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QTimer, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsDropShadowEffect,
                               QHBoxLayout, QLabel, QMainWindow, QSizePolicy,
                               QWidget)
from ui_main import Ui_MainWindow
from ui_splash_screen import Ui_SplashScreen
from widgets import CircularProgress

# Counter
counter = 0


class SplashScreen(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # Remove Title bar
        self.setWindowFlags(Qt.FramelessWindowHint)  # type: ignore
        self.setAttribute(Qt.WA_TranslucentBackground)  # type: ignore


        self.progress = CircularProgress()
        self.progress.width = 270  # type: ignore
        self.progress.height = 270  # type: ignore
        self.progress.value = 50
        self.progress.setFixedSize(self.progress.width,  # type: ignore
                                   self.progress.height)
        self.progress.move(15, 15)
        self.progress.font_size = 20
        self.progress.addShadow(True)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()
    
        self.show()

        # Add SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.setGraphicsEffect(self.shadow)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

    # Update progress bar
    def update(self):
        global counter

        # Set value to progress bar
        self.progress.setValue(counter)

        # Stop counter
        if counter >= 100:
            self.timer.stop()

            # Open a new Window
            self.main = MainWindow()
            self.main.show()

            # Close Splash Screen
            self.close()

        # Increases counter
        counter += 1


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication()
    window = SplashScreen()
    sys.exit(app.exec())