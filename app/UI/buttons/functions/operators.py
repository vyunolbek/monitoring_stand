import os
import json
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class Operator(object):

    def __init__(self):
        self.push_lineedit = "QLineEdit {background-color: #1a1c20; color: white; border-radius: 10px;}"
        self.hover_lineedit = "QLineEdit:hover {background-color: #f0a500; color: white;}"
        self.pressed_lineedit = "QLineEdit:pressed {background-color: #1a1c20; color: white;}"
        self.push_button = "QPushButton {background-color: #1a1c20; color: white; border-radius: 10px;}"
        self.hover_button = "QPushButton:hover {background-color: #f0a500; color: white;}"
        self.pressed_button = "QPushButton:pressed {background-color: #1a1c20; color: white;}"
    
    
    def operator_lineedit(self):
        """Operator lineedit."""
        self.operator_lineedit = QLineEdit()
        self.operator_lineedit.setFixedSize(250, 50)
        self.operator_lineedit.setFont(QFont("Arial", 14))
        self.operator_lineedit.setStyleSheet(f"{self.push_lineedit}{self.hover_lineedit}{self.pressed_lineedit}")
        self.operator_lineedit.setPlaceholderText("Введите имя оператора")
        self.operator_lineedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.operator_lineedit.setMaxLength(20)
        return self.operator_lineedit
    
    def __operator_changed(self):
        """Operator lineedit changed."""
        self.operator_label.setText(self.operator_lineedit.text())
        self.operator_label.show()
        self.operator_lineedit.hide()
        self.save_button.show()
        self.cancel_button.show()


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
