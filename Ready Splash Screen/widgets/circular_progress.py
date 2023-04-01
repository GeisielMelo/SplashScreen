from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QColor, QFont, QPainter, QPen
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QWidget


class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Custom Properties
        self.value = 0
        self.width = 200  # type: ignore
        self.height = 200  # type: ignore
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x498BD1
        self.max_value = 100
        
        self.enable_text = True
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0x498BD1
        self.enable_shadow = False

        self.enable_bg = False
        self.bg_color = 0x44475a

        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.resize(self.width, self.height)

    # Add SHADOW
    def addShadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)

    # SET VALUE
    def setValue(self, value):
        self.value = value
        self.repaint()

    # PAINT EVENT
    def paintEvent(self, event):
        # Set Progress Parameters
        width = self.width - self.progress_width    # type: ignore
        height = self.height - self.progress_width  # type: ignore
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        # Painter
        paint = QPainter()
        paint.begin(self)
        # paint.setRenderHint(QPainter.Antialiasing) remove pixeled edges
        paint.setRenderHint(QPainter.Antialiasing)   # type: ignore
        paint.setFont(QFont(self.font_family, self.font_size))

        # Create rectangle
        rect = QRect(0, 0, self.width, self.height)  # type: ignore
        paint.setPen(Qt.NoPen)  # type: ignore
        paint.drawRect(rect)

        # Pen
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)  # type: ignore

        # Enable bg
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            paint.drawArc(margin, margin, width, height, 0, 360 * 16)

        # Create ARC / Circular progress
        paint.setPen(pen)
        paint.drawArc(margin, margin, width,  # type: ignore
                      height, -90 * 16, -value * 16)  # type: ignore

        # Creating Text
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(
            rect, Qt.AlignCenter, f"{self.value}{self.suffix}")  # type: ignore

        # End
        paint.end()
