import os
import json
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont


class Operator(object):

    def __init__(self):
        self.operators: list = ["+ Добавить нового оператора"]
        self.push = "QComboBox {background-color: #d6d6d6; color: black; border-radius: 10px;}"
        self.hover = "QComboBox:hover {background-color: #b3b3b3; color: white;}"
        self.pressed = "QComboBox:pressed {background-color: #999999; color: white;}"


    def __get_operators(self) -> None:
        """Get operators from json file."""
        for filename in os.listdir("operators"):
            if filename.endswith('.json'):
                file_path = os.path.join("operators", filename)
                with open(file_path, 'r') as file:
                    content = json.load(file)
                    self.operators.append(content["operator"])

    
    def select_operator(self) -> QComboBox:
        """Select operator."""
        self.__get_operators()
        self.select_operator = QComboBox()
        self.select_operator.setFixedSize(300, 50)
        self.select_operator.setFont(QFont("Arial", 14))
        self.select_operator.addItems(self.operators)
        self.select_operator.setStyleSheet(f"{self.push}{self.hover}{self.pressed}")
        return self.select_operator
