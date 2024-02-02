from PyQt6.QtWidgets import *
from UI.buttons.design import ButtonsDesign as bd


class Buttons(object):

    def save_button() -> QPushButton:
        """Save button."""
        button = QPushButton("Сохранить")
        bd(button).save_button()
        return button
    

    def cancel_button() -> QPushButton:
        """Cancel button."""
        button = QPushButton("Отмена")
        bd(button).cancel_button()
        return button


    def create_markup_button() -> QPushButton:
        """Create markup button."""
        button = QPushButton("Сделать разметку")
        bd(button).create_markup_button()
        return button


    def save_markup_button() -> QPushButton:
        """Save markup button."""
        button = QPushButton("Сохранить разметку")
        bd(button).save_markup_button()
        return button


    def upload_markup_button() -> QPushButton:
        """Upload markup button."""
        button = QPushButton("Загрузить разметку")
        bd(button).upload_markup_button()
        return button


    def check_markup_button() -> QPushButton:
        """Check markup button."""
        button = QPushButton("Проверить разметку")
        bd(button).check_markup_button()
        return button


    def select_operator_button() -> QPushButton:
        """Select operator button."""
        button = QPushButton("Выбрать оператора")
        bd(button).select_operator_button()
        return button
