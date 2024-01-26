from typing import Any
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ButtonsDesign(object):

    def __init__(self, button: QPushButton):
        self.button = button
        self.width, self.height = 250, 50
        self.type_font, self.size_font = "Arial", 15
        self.push = "QPushButton {background-color: #1a1c20; color: white; border-radius: 10px;}"
        self.hover = "QPushButton:hover {background-color: #f0a500; color: white;}"
        self.pressed = "QPushButton:pressed {background-color: #cf7500; color: white;}"


    def create_markup_button(self) -> QPushButton:
        """Create markup button design"""
        self.button.setFixedSize(self.width, self.height)
        self.button.setFont(QFont(self.type_font, self.size_font))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def save_markup_button(self) -> QPushButton:
        """Save markup button design"""
        self.button.setFixedSize(self.width, self.height)
        self.button.setFont(QFont(self.type_font, self.size_font))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def upload_markup_button(self) -> QPushButton:
        """Upload markup button design"""
        self.button.setFixedSize(self.width, self.height)
        self.button.setFont(QFont(self.type_font, self.size_font))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def check_markup_button(self) -> QPushButton:
        """Check markup button design"""
        self.button.setFixedSize(self.width, self.height)
        self.button.setFont(QFont(self.type_font, self.size_font))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def select_operator_button(self) -> QPushButton:
        """Select operator button design"""
        self.button.setFixedSize(self.width, self.height)
        self.button.setFont(QFont(self.type_font, self.size_font))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button


    def create_button(self) -> QPushButton:
        """Create button design"""
        self.button.setFixedSize(self.width, self.height)
        self.button.setFont(QFont(self.type_font, self.size_font))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def save_button(self) -> QPushButton:
        """Save button design"""
        self.button.setFixedSize(self.width, self.height)
        self.button.setFont(QFont(self.type_font, self.size_font))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def select_button(self) -> QPushButton:    
        """Select button design"""
        self.button.setFixedSize(self.width, self.height)
        self.button.setFont(QFont(self.type_font, self.size_font))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
    

    def cancel_button(self) -> QPushButton:
        """Cancel button design"""
        self.button.setFixedSize(self.width, self.height)
        self.button.setFont(QFont(self.type_font, self.size_font))
        self.button.setStyleSheet(f"{self.push} {self.hover} {self.pressed}")
        return self.button
