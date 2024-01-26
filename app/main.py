import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import QtCore, QtGui, QtWidgets, uic

from UI.buttons.create import Buttons as bttns
from UI.buttons.functions.operators import Operator as slct_oprtr
from UI.labels.create import Labels as lbls
from UI.pixmap.create import Pixmap as pxmp
from UI.widgets.create import Widgets as wdts


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.width, self.height = 1900, 1050
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle("Optical control stand")
        self.img_path = "imgs/base/test1.jpg"

        central_widget = wdts.main_widget(self)
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout(central_widget)
        self.layout.setSpacing(5)

        self.operator_label = lbls(operator="None",
                                   width=self.width).operator_label()
        self.layout.addWidget(self.operator_label, 
                              alignment=Qt.AlignmentFlag.AlignCenter)

        self.img_label = QLabel()
        self.img_label = pxmp(img_path=self.img_path, 
                              window_width=self.width, 
                              window_height=self.height, 
                              img_label=self.img_label).img_pixmap_main()
        self.layout.addWidget(self.img_label, 
                              alignment=Qt.AlignmentFlag.AlignCenter)

        self.create_markup_button = bttns.create_markup_button()
        self.layout.addWidget(self.create_markup_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        self.create_markup_button.clicked.connect(self.__create_markup)

        self.save_markup_button = bttns.save_markup_button()
        self.layout.addWidget(self.save_markup_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        self.save_markup_button.clicked.connect(self.__save_markup)

        self.upload_markup_button = bttns.upload_markup_button()
        self.layout.addWidget(self.upload_markup_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        self.upload_markup_button.clicked.connect(self.__upload_markup)

        self.check_markup_button = bttns.check_markup_button()
        self.layout.addWidget(self.check_markup_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        self.check_markup_button.clicked.connect(self.__check_markup)

        self.select_operator_button = bttns.select_operator_button()
        self.layout.addWidget(self.select_operator_button, 
                              alignment=Qt.AlignmentFlag.AlignLeft)
        self.select_operator_button.clicked.connect(self.__select_operator)

    
    def __buttons_list(self) -> list:
        return [self.create_markup_button,
                self.save_markup_button,
                self.upload_markup_button,
                self.check_markup_button,
                self.select_operator_button]

    
    def __create_markup(self) -> None:
        for button in self.__buttons_list():
            button.hide()
        
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

        self.save_button = bttns.save_button()
        self.layout.addWidget(self.save_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.cancel_button = bttns.cancel_button()
        self.layout.addWidget(self.cancel_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        

    def __save_markup(self) -> None:
        pass


    def __upload_markup(self) -> None:
        pass


    def __check_markup(self) -> None:
        pass


    def __select_operator(self) -> None:
        self.img_label.hide()
        for button in self.__buttons_list():
            button.hide()
        
        self.create_operator_button = slct_oprtr().create_operator_button()
        self.layout.addWidget(self.create_operator_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)

        self.select_operator_button = slct_oprtr().select_operator_button()
        self.layout.addWidget(self.select_operator_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.back_button = slct_oprtr().back_button()
        self.layout.addWidget(self.back_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.layout.addStretch(10)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
