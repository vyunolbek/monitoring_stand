import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

from UI.buttons.create import Buttons as bttns
from UI.buttons.functions.operators import Operator as slct_oprtr
from UI.labels.create import Labels as lbls
from UI.pixmap.create import Pixmap as pxmp
from UI.widgets.create import Widgets as wdts


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.width, self.height = 1250, 1000
        self.setWindowTitle("Optical control stand")
        self.img_path = "imgs/base/test1.jpg"

        central_widget = wdts.main_widget(self)
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout(central_widget)

        self.operator_label = lbls("None").operator_label()
        self.layout.addWidget(self.operator_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.img_label = QLabel(self)
        self.img_label = pxmp(self.img_path, self.width, self.height, self.img_label).img_pixmap()
        self.layout.addWidget(self.img_label)

        self.create_markup_button = bttns.create_markup_button()
        self.layout.addWidget(self.create_markup_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.create_markup_button.clicked.connect(lambda: print("create_markup_button"))

        self.save_markup_button = bttns.save_markup_button()
        self.layout.addWidget(self.save_markup_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.save_markup_button.clicked.connect(lambda: print("save_markup_button"))

        self.upload_markup_button = bttns.upload_markup_button()
        self.layout.addWidget(self.upload_markup_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.upload_markup_button.clicked.connect(lambda: print("upload_markup_button"))

        self.check_markup_button = bttns.check_markup_button()
        self.layout.addWidget(self.check_markup_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.check_markup_button.clicked.connect(lambda: print("check_markup_button"))

        self.select_operator_button = bttns.select_operator_button()
        self.layout.addWidget(self.select_operator_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.select_operator_button.clicked.connect(self.__select_operator)

        self.showMaximized()
        

    def __select_operator(self) -> None:
        self.img_label.hide()
        self.create_markup_button.hide()
        self.save_markup_button.hide()
        self.upload_markup_button.hide()
        self.check_markup_button.hide()
        self.select_operator_button.hide()

        self.ranmdom_label = QLabel(self)
        self.ranmdom_label.setFixedSize(100, 100)
        self.layout.addWidget(self.ranmdom_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.select_operator_box = slct_oprtr().select_operator()
        self.layout.addWidget(self.select_operator_box, alignment=Qt.AlignmentFlag.AlignCenter)

        self.select_button = bttns.select_button()
        self.layout.addWidget(self.select_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.layout.addStretch(2)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
