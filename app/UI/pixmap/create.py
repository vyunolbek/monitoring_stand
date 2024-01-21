from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from UI.pixmap.design import PixmapDesign as pd
from UI.pixmap.imgs_resize import ImagesResize as ir


class Pixmap(object):

    def __init__(self, img_path: str, window_width: int, window_height: int, img_label: QLabel):
        self.img_path = img_path
        self.window_width = window_width
        self.window_height = window_height
        self.img_label = img_label
    

    def img_pixmap(self) -> QLabel:
        """Create pixmap for image label."""
        resized_img = ir(img_path=self.img_path,
                         window_width=self.window_width,
                         window_height=self.window_height).resize_image()
        
        pixmap = QPixmap(resized_img)  
        self.img_label.setPixmap(pixmap)
        pd.img_pixmap(self.img_label)
        return self.img_label
