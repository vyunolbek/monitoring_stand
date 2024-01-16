from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import sys

from buttons.create import Buttons as bttns


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("App")
        self.main_layout = QVBoxLayout()

        pixmap = QPixmap("./imgs/test2.jpg")  
        image_label = QLabel(self)
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        self.main_layout.addWidget(image_label)

        buttons_layout = QHBoxLayout()
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        buttons_layout.setSpacing(5)

        select_image_button = bttns.select_image_button()
        load_image_button = bttns.load_image_button()
        load_coordinates_button = bttns.load_coordinates_button()
        save_coordinates_button = bttns.save_coordinates_button()
        check_button = bttns.check_button()

        buttons_layout.addWidget(select_image_button)
        buttons_layout.addWidget(load_image_button)
        buttons_layout.addWidget(load_coordinates_button)
        buttons_layout.addWidget(save_coordinates_button)
        buttons_layout.addWidget(check_button)

        self.main_layout.addLayout(buttons_layout)

        central_widget = QWidget(self)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        self.left, self.top, self.width, self.height = 1100, 100, 800, 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet("background-color: #ffffff;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
