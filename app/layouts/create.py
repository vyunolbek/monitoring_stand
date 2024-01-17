from PyQt6.QtWidgets import *
from layouts.design import LayoutsDesign as ld


class Layouts(object):

    @staticmethod
    def buttons_layout() -> QHBoxLayout:
        layout = QHBoxLayout()
        layout = ld.buttons_layout(layout)
        return layout
