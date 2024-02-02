import sys
from PIL import Image
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import QPoint
from PyQt6 import QtCore, QtGui

from UI.buttons.create import Buttons as bttns
from UI.buttons.functions.operators import Operator as slct_oprtr
from UI.labels.create import Labels as lbls
from UI.pixmap.create import Pixmap as pxmp
from UI.widgets.create import Widgets as wdts


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.flag: str = ""
        self.width, self.height = 1900, 1050
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle("Optical control stand")
        self.img_path = "imgs/base/test1.jpg"

        self.central_widget = wdts.main_widget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(5)

        self.operator_label = lbls(operator="None",
                                   width=self.width).operator_label()
        self.layout.addWidget(self.operator_label, 
                              alignment=Qt.AlignmentFlag.AlignCenter)

        self.img_label = QLabel()
        self.img_label = pxmp(img_path=self.img_path, 
                              window_width=self.width, 
                              window_height=self.height, 
                              img_label=self.img_label).img_pixmap()
        self.layout.addWidget(self.img_label, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.img_markup_label = QLabel()
        self.img_markup_label = pxmp(img_path=self.img_path,
                                        window_width=self.width,
                                        window_height=self.height,
                                        img_label=self.img_markup_label).img_pixmap_markup()
        self.layout.addWidget(self.img_markup_label, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        self.img_markup_label.hide()
        
        self.operator_lineedit = slct_oprtr().operator_lineedit()
        self.layout.addWidget(self.operator_lineedit, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        self.operator_lineedit.hide()

        self.save_button = bttns.save_button()
        self.layout.addWidget(self.save_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        self.save_button.hide()
        
        self.cancel_button = bttns.cancel_button()
        self.layout.addWidget(self.cancel_button, 
                              alignment=Qt.AlignmentFlag.AlignCenter)
        self.cancel_button.hide()

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
        

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.start_pos = e.position()


    def mouseMoveEvent(self, e):
        if self.start_pos is not None:
            canvas = self.img_markup_label.pixmap()
            painter = QtGui.QPainter(canvas)
            painter.setPen(QtGui.QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.SolidLine))
            rect = QtCore.QRect(int(self.start_pos.x()), int(self.start_pos.y()), int(e.position().x() - self.start_pos.x()), int(e.position().y() - self.start_pos.y())).normalized()
            painter.drawRect(rect)
            painter.end()
            self.img_markup_label.setPixmap(canvas)


    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.start_pos = None


    def __create_markup(self) -> None:
        """Create markup button action."""
        self.flag = "create_markup"
        for button in self.__buttons_list():
            button.hide()
        self.img_label.hide()

        self.img_markup_label.show()
        self.save_button.show()
        self.cancel_button.show()
        self.cancel_button.clicked.connect(self.__cancel_button)
        
        self.layout.addStretch(10)


    def __save_markup(self) -> None:
        pass


    def __upload_markup(self) -> None:
        pass


    def __check_markup(self) -> None:
        pass


    def __select_operator(self) -> None:
        """Select operator button action."""
        self.flag = "select_operator"
        self.img_label.hide()
        for button in self.__buttons_list():
            button.hide()

        self.operator_lineedit.show()
        self.save_button.show()
        self.cancel_button.show()
        self.cancel_button.clicked.connect(self.__cancel_button)
        
        self.layout.addStretch(5)

    
    def __cancel_button(self) -> None:
        """Cancel button action."""
        if self.flag == "create_markup":
            self.flag = ""
            self.save_button.hide()
            self.cancel_button.hide()
            self.img_markup_label.hide()
            for button in self.__buttons_list():
                button.show()
            self.img_label.show()
            self.layout.addStretch(5)
        elif self.flag == "select_operator":
            self.flag = ""
            self.operator_lineedit.hide()
            self.save_button.hide()
            self.cancel_button.hide()
            self.img_label.show()
            for button in self.__buttons_list():
                button.show()
            self.layout.addStretch(5)
        else:
            pass
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
