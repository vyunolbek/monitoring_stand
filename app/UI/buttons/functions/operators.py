import os
import json
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont


class Operator(object):

    def __init__(self):
        self.push_box = "QComboBox {background-color: #1a1c20; color: white; border-radius: 10px;}"
        self.hover_box = "QComboBox:hover {background-color: #f0a500; color: white;}"
        self.pressed_box = "QComboBox:pressed {background-color: #1a1c20; color: white;}"
        self.push_button = "QPushButton {background-color: #1a1c20; color: white; border-radius: 10px;}"
        self.hover_button = "QPushButton:hover {background-color: #f0a500; color: white;}"
        self.pressed_button = "QPushButton:pressed {background-color: #1a1c20; color: white;}"


    def clicked_create_operator(self) -> None:
        self.create_operator.hide()
        self.select_operator.hide()
        self.back_button.hide()

        self.operator_name = QLineEdit()
        self.operator_name.setFixedSize(300, 50)
        self.operator_name.setFont(QFont("Arial", 14))
        self.operator_name.setStyleSheet(f"{self.push_box}{self.hover_box}{self.pressed_box}")
        return self.operator_name
    

    def create_operator_button(self) -> QPushButton:
        """Create operator button."""
        self.create_operator = QPushButton("Create operator")
        self.create_operator.setFixedSize(300, 50)
        self.create_operator.setFont(QFont("Arial", 14))
        self.create_operator.setStyleSheet(f"{self.push_button}{self.hover_button}{self.pressed_button}")
        return self.create_operator

    def __get_operators(self) -> list:
        """Get operators from json file."""
        operators = ["None"]

        for filename in os.listdir("operators"):
            if filename.endswith('.json'):
                file_path = os.path.join("operators", filename)
                with open(file_path, 'r') as file:
                    content = json.load(file)
                    operators.append(content["operator"])

        return operators

    def clicked_select_operator_button(self) -> None:
        """Click select operator button."""
        self.create_operator.hide()
        self.select_operator.hide()
        self.back_button.hide()

        self.operators_box = QComboBox()
        self.operators_box.setFixedSize(300, 50)
        self.operators_box.setFont(QFont("Arial", 14))
        self.operators_box.addItems(self.__get_operators())
        self.operators_box.setStyleSheet(f"{self.push_box}{self.hover_box}{self.pressed_box}")
        return self.operators_box


    def select_operator_button(self) -> QPushButton:
        """Select operator button."""
        self.select_operator = QPushButton("Select operator")
        self.select_operator.setFixedSize(300, 50)
        self.select_operator.setFont(QFont("Arial", 14))
        self.select_operator.setStyleSheet(f"{self.push_button}{self.hover_button}{self.pressed_button}")
        return self.select_operator
    

    def clicked_back_button(self) -> None:
        """Click back button."""
        pass


    def back_button(self) -> QPushButton:
        """Back button."""
        self.back_button = QPushButton("Back")
        self.back_button.setFixedSize(300, 50)
        self.back_button.setFont(QFont("Arial", 14))
        self.back_button.setStyleSheet(f"{self.push_button}{self.hover_button}{self.pressed_button}")
        return self.back_button  