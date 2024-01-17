from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class LayoutsDesign(object):

    def buttons_layout(layout: QHBoxLayout) -> QHBoxLayout:
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return layout