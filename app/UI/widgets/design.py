from PyQt6.QtWidgets import *


class WidgetsDesign(object):

    @staticmethod
    def main_widget(widget: QWidget) -> QWidget:
        widget.setStyleSheet("background-color: #f4f4f4;")
        return widget