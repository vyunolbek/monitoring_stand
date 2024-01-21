from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class PixmapDesign(object):

    @staticmethod
    def img_pixmap(img_label: QLabel) -> QLabel:
        """Set design for image label."""
        img_label.setScaledContents(True)
        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return img_label
