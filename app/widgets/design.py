from PyQt6.QtWidgets import *


class WidgetDesign(object):

    def buttons_widget(widget: QWidget) -> QWidget:
        widget.setFixedSize(800, 600)
        widget.setStyleSheet("background-color: #FFFFFF;")
        return widget
