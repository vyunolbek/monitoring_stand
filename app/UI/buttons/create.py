from PyQt6.QtWidgets import *
from UI.buttons.design import ButtonsDesign as bd


class Buttons(object):

    def create_markup_button() -> QPushButton:
        button = QPushButton("Сделать разметку")
        bd(button).create_markup_button()
        return button


    def save_markup_button() -> QPushButton:
        button = QPushButton("Сохранить разметку")
        bd(button).save_markup_button()
        return button


    def upload_markup_button() -> QPushButton:
        button = QPushButton("Загрузить разметку")
        bd(button).upload_markup_button()
        return button


    def check_markup_button() -> QPushButton:
        button = QPushButton("Проверить разметку")
        bd(button).check_markup_button()
        return button


    def select_operator_button() -> QPushButton:
        button = QPushButton("Выбрать оператора")
        bd(button).select_operator_button()
        return button
