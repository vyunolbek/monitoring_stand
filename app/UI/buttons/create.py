from PyQt6.QtWidgets import *
from UI.buttons.design import ButtonsDesign as bd


class Buttons(object):

    @staticmethod
    def create_markup_button() -> QPushButton:
        button = QPushButton("Сделать разметку")
        bd(button).create_markup_button()
        return button


    @staticmethod
    def save_markup_button() -> QPushButton:
        button = QPushButton("Сохранить разметку")
        bd(button).save_markup_button()
        return button


    @staticmethod
    def upload_markup_button() -> QPushButton:
        button = QPushButton("Загрузить разметку")
        bd(button).upload_markup_button()
        return button


    @staticmethod
    def check_markup_button() -> QPushButton:
        button = QPushButton("Проверить разметку")
        bd(button).check_markup_button()
        return button


    @staticmethod
    def select_operator_button() -> QPushButton:
        button = QPushButton("Выбрать оператора")
        bd(button).select_operator_button()
        return button
    

    @staticmethod
    def create_new_operator_button() -> QPushButton:
        button = QPushButton("Создать оператора")
        bd(button).create_new_operator_button()
        return button
    

    @staticmethod
    def create_button() -> QPushButton:
        button = QPushButton("Создать")
        bd(button).create_button()
        return button
    

    @staticmethod
    def select_button() -> QPushButton:
        button = QPushButton("Выбрать")
        bd(button).select_button()
        return button
    

    @staticmethod
    def cancel_button() -> QPushButton:
        button = QPushButton("Отмена")
        bd(button).cancel_button()
        return button
