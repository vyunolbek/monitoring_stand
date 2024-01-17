from PyQt6.QtWidgets import *


class PixmapDesign(object):

    def image_pixmap(image_label: QLabel) -> QLabel:
        image_label.setScaledContents(True)
        return image_label
