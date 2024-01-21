from PyQt6.QtWidgets import *
from UI.widgets.design import WidgetsDesign as wd


class Widgets(object):

    @staticmethod
    def main_widget(self) -> QWidget:
        main_widget = QWidget(self)
        main_widget = wd.main_widget(main_widget)
        return main_widget
