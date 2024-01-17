from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from pixmap.design import PixmapDesign as pd


class Pixmap(object):

    def image_pixmap(image_path: str) -> QLabel:
        pixmap = QPixmap(image_path)  
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        pd.image_pixmap(image_label)
        return image_label
