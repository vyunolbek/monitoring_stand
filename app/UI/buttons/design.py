from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ButtonsDesign(object):

    def __init__(self, button: QPushButton):
        self.button = button
        self.width, self.height = 200, 40
        self.push = "QPushButton {background-color: #d6d6d6; color: black; border-radius: 10px;}"
        self.hover = "QPushButton:hover {background-color: #b3b3b3; color: white;}"
        self.pressed = "QPushButton:pressed {background-color: #999999; color: white;}"


    def create_markup_button(self) -> QPushButton:
        self.button.setFixedSize(200, 40)
        self.button.setFont(QFont("Arial", 15))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def save_markup_button(self) -> QPushButton:
        self.button.setFixedSize(200, 40)
        self.button.setFont(QFont("Arial", 15))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def upload_markup_button(self) -> QPushButton:
        self.button.setFixedSize(200, 40)
        self.button.setFont(QFont("Arial", 15))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def check_markup_button(self) -> QPushButton:
        self.button.setFixedSize(200, 40)
        self.button.setFont(QFont("Arial", 15))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def select_operator_button(self) -> QPushButton:
        self.button.setFixedSize(200, 40)
        self.button.setFont(QFont("Arial", 15))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def create_new_operator_button(self) -> QPushButton:
        self.button.setFixedSize(200, 40)
        self.button.setFont(QFont("Arial", 15))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button


    def create(self) -> QPushButton:
        self.button.setFixedSize(100, 40)
        self.button.setFont(QFont("Arial", 15))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def cancel(self) -> QPushButton:
        self.button.setFixedSize(100, 40)
        self.button.setFont(QFont("Arial", 15))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button