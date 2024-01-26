from PyQt6.QtWidgets import *


class PixmapDesign(object):

    @staticmethod
    def img_pixmap_main(img_label: QLabel, width: int, height: int) -> QLabel:
        """Set design for image label."""
        img_label.setFixedSize(int(width // 1.5), int(height // 1.5))
        img_label.setScaledContents(True)
        return img_label
    
    
    @staticmethod
    def img_pixmap_markup(img_label: QLabel, width: int, height: int) -> QLabel:
        """Set design for image label."""
        img_label.setFixedSize(int(width // 1.3), int(height // 1.3))
        img_label.setScaledContents(True)
        return img_label
