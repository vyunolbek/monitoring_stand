from PyQt6.QtWidgets import *
from widgets.design import WidgetDesign as wd


class Widgets(object):

    @staticmethod
    def buttons_widget() -> QWidget:
        widget = QWidget()
        widget = wd.buttons_widget(widget)
        return widget
