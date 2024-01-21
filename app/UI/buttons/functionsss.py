import os
import json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog
from UI.buttons.create import Buttons as bttns


class ButtonsFunctions(object):

    def select_img_path() -> str:
        """Select image path."""
        img_path, _ = QFileDialog.getOpenFileName(
            caption="Выберите изображение",
            filter="Image files (*.jpg *.png)"
        )
        return img_path
    

    def select_markup_path() -> str:
        """Select markup path."""
        markup_path, _ = QFileDialog.getOpenFileName(
            caption="Выберите разметку",
            filter="Markup files (*.json)"
        )
        return markup_path
    

    def select_operator(self):

        class SelectOperator(QDialog):
            def __init__(self):
                super().__init__()
                self.left, self.top, self.width, self.height = 1100, 100, 300, 200
                self.setGeometry(self.left, self.top, self.width, self.height)
                self.setFixedSize(self.width, self.height)
                self.setWindowTitle("Выбор оператора")

                self.layout = QVBoxLayout(self)

                self.create_new_operator = bttns.create_new_operator_button()
                self.create_new_operator.clicked.connect(self.__new_operator)
                self.layout.addWidget(self.create_new_operator, alignment=Qt.AlignmentFlag.AlignCenter)

                self.select_operator = bttns.select_operator_button()
                self.select_operator.clicked.connect(self.__select_operator)
                self.layout.addWidget(self.select_operator, alignment=Qt.AlignmentFlag.AlignCenter)

            
            def __new_operator(self):
                self.create_new_operator.hide()
                self.select_operator.hide()

                self.new_operator_label = QLabel("Введите нового оператора:")
                self.layout.addWidget(self.new_operator_label)

                self.new_operator_line = QLineEdit()
                self.layout.addWidget(self.new_operator_line)

                self.create_button = bttns.create()
                self.layout.addWidget(self.create_button)

                self.cancel_button = bttns.cancel()
                self.layout.addWidget(self.cancel_button)

                self.create_button.clicked.connect(self.__create_new_operator)


            def __create_new_operator(self):
                operator = self.new_operator_line.text()
                data = {"operator": operator}
                json.dump(data, open(f"operators/[{operator}].json", "w"))
                self.close()


            def __select_operator(self):
                operators = []
                for filename in os.listdir("operators"):
                    if filename.endswith('.json'):
                        file_path = os.path.join("operators", filename)
                        with open(file_path, 'r') as file:
                            content = json.load(file)
                            operators.append(content["operator"])
                            
                self.select_operator.hide()
                self.create_new_operator.hide()

                self.operators_label = QLabel("Выберите оператора:")
                self.layout.addWidget(self.operators_label)

                self.operators_combo = QComboBox()
                self.operators_combo.addItems(operators)
                self.layout.addWidget(self.operators_combo)







        SelectOperator().exec()
