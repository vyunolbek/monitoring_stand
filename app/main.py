from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
import sys

from pixmap.create import Pixmap as pxmp
from layouts.create import Layouts as lyts
from widgets.create import Widgets as wdgts
from buttons.create import Buttons as bttns


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.left, self.top, self.width, self.height = 1100, 100, 800, 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle("Optical control stand")

        self.main_layout = QVBoxLayout()

        self.image_label = pxmp.image_pixmap("../imgs/test2.jpg")

        self.buttons_layout = lyts.buttons_layout()

        buttons = [bttns.create_markup_button(),
                   bttns.save_markup_button(),
                   bttns.upload_markup_button(),
                   bttns.check_markup_button(),
                   bttns.select_operator_button()]

        for button in buttons:
            self.buttons_layout.addWidget(button)

        self.main_layout.addWidget(self.image_label)
        self.main_layout.addLayout(self.buttons_layout)

        self.buttons_widget = wdgts.buttons_widget()
        self.buttons_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.buttons_widget)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
