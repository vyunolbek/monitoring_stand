import os
import json
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont


class Operator(object):

    def __init__(self):
        self.push_lineedit = "QLineEdit {background-color: #1a1c20; color: white; border-radius: 10px;}"
        self.hover_lineedit = "QLineEdit:hover {background-color: #f0a500; color: white;}"
        self.pressed_lineedit = "QLineEdit:pressed {background-color: #1a1c20; color: white;}"
        self.push_box = "QComboBox {background-color: #1a1c20; color: white; border-radius: 10px;}"
        self.hover_box = "QComboBox:hover {background-color: #f0a500; color: white;}"
        self.pressed_box = "QComboBox:pressed {background-color: #1a1c20; color: white;}"
        self.push_button = "QPushButton {background-color: #1a1c20; color: white; border-radius: 10px;}"
        self.hover_button = "QPushButton:hover {background-color: #f0a500; color: white;}"
        self.pressed_button = "QPushButton:pressed {background-color: #1a1c20; color: white;}"


    def create_button(self) -> QPushButton:
        """Create button."""
        self.create_button = QPushButton("Создать")
        self.create_button.setFixedSize(300, 50)
        self.create_button.setFont(QFont("Arial", 14))
        self.create_button.setStyleSheet(f"{self.push_button}{self.hover_button}{self.pressed_button}")
        return self.create_button
    
    
    def operator_lineedit(self) -> QLineEdit:
        """Operator lineedit."""
        self.operator_lineedit = QLineEdit()
        self.operator_lineedit.setFixedSize(300, 50)
        self.operator_lineedit.setFont(QFont("Arial", 14))
        self.operator_lineedit.setStyleSheet(f"{self.push_lineedit}{self.hover_lineedit}{self.pressed_lineedit}")
        return self.operator_lineedit

    def create_operator_button(self) -> QPushButton:
        """Create operator button."""
        self.create_operator = QPushButton("Создать оператора")
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


    def select_operator_button(self) -> QPushButton:
        """Select operator button."""
        self.select_operator = QPushButton("Выбрать оператора")
        self.select_operator.setFixedSize(300, 50)
        self.select_operator.setFont(QFont("Arial", 14))
        self.select_operator.setStyleSheet(f"{self.push_button}{self.hover_button}{self.pressed_button}")
        return self.select_operator


    def back_button(self) -> QPushButton:
        """Back button."""
        self.back_button = QPushButton("Назад")
        self.back_button.setFixedSize(300, 50)
        self.back_button.setFont(QFont("Arial", 14))
        self.back_button.setStyleSheet(f"{self.push_button}{self.hover_button}{self.pressed_button}")
        return self.back_button  
