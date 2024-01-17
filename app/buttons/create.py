from PyQt6.QtWidgets import *
from buttons.design import ButtonsDesign as bd


class Buttons(object):

    @staticmethod
    def create_markup_button() -> QPushButton:
        button = QPushButton("Сделать разметку")
        bd.create_markup_button(button)
        return button


    @staticmethod
    def save_markup_button() -> QPushButton:
        button = QPushButton("Сохранить разметку")
        bd.save_markup_button(button)
        return button


    @staticmethod
    def upload_markup_button() -> QPushButton:
        button = QPushButton("Загрузить разметку")
        bd.upload_markup_button(button)
        return button


    @staticmethod
    def check_markup_button() -> QPushButton:
        button = QPushButton("Проверить разметку")
        bd.check_markup_button(button)
        return button


    @staticmethod
    def select_operator_button() -> QPushButton:
        button = QPushButton("Выбрать оператора")
        bd.select_operator_button(button)
        return button
