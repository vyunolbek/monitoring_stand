from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ButtonsDesign(object):

    def create_markup_button(button: QPushButton) -> QPushButton:
        button.setFixedSize(140, 40)
        button.setStyleSheet("background-color: #d6d6d6; color: black; border-radius: 10px;")
        return button
    

    def save_markup_button(button: QPushButton) -> QPushButton:
        button.setFixedSize(140, 40)
        button.setStyleSheet("background-color: #d6d6d6; color: black; border-radius: 10px;")
        return button
    

    def upload_markup_button(button: QPushButton) -> QPushButton:
        button.setFixedSize(140, 40)
        button.setStyleSheet("background-color: #d6d6d6; color: black; border-radius: 10px;")
        return button
    

    def check_markup_button(button: QPushButton) -> QPushButton:
        button.setFixedSize(140, 40)
        button.setStyleSheet("background-color: #d6d6d6; color: black; border-radius: 10px;")
        return button
    

    def select_operator_button(button: QPushButton) -> QPushButton:
        button.setFixedSize(140, 40)
        button.setStyleSheet("background-color: #d6d6d6; color: black; border-radius: 10px;")
        return button
