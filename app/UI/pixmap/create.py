from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtGui
from UI.pixmap.design import PixmapDesign as pd
from UI.pixmap.imgs_resize import ImagesResize as ir


class Pixmap(object):

    def __init__(self, img_path: str, window_width: int, window_height: int, img_label: QLabel):
        self.img_path: str = img_path
        self.window_width: int = window_width
        self.window_height: int = window_height
        self.img_label: QLabel = img_label
    

    def img_pixmap(self) -> QLabel:
        """Create pixmap for image label."""
        resized_img, ratio = ir(img_path=self.img_path,
                         window_width=self.window_width,
                         window_height=self.window_height).resize_image()
        
        pixmap = QPixmap(resized_img)  
        self.img_label.setPixmap(pixmap)
        pd.img_pixmap(self.img_label, self.window_width, self.window_height)
        return self.img_label
    

    def img_pixmap_markup(self) -> QLabel:
        """Create pixmap for markup label."""
        resized_img, ratio = ir(img_path=self.img_path,
                         window_width=self.window_width,
                         window_height=self.window_height).resize_image()
        
        canvas = QtGui.QPixmap(resized_img)
        self.img_label.setPixmap(canvas)
        pd.img_pixmap_markup(self.img_label, self.window_width, self.window_height)
        return self.img_label
