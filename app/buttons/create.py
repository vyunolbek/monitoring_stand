from PyQt6.QtWidgets import *


class Buttons(object):

    def select_image_button() -> QPushButton:
        button = QPushButton("Выбрать изображение")
        return button
    
    
    def load_image_button() -> QPushButton:
        button = QPushButton("Загрузить изображение")
        return button
    

    def load_coordinates_button() -> QPushButton:
        button = QPushButton("Загрузить координаты")
        return button
    

    def save_coordinates_button() -> QPushButton:
        button = QPushButton("Сохранить координаты")
        return button
    

    def check_button() -> QPushButton:
        button = QPushButton("Проверить")
        return button
    