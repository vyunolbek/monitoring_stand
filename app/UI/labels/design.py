from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class DesignLabels(object):

    def operator_label(operator_label: QLabel, width: int) -> QLabel:
        operator_label.setStyleSheet("font-size: 20px; color: black;")
        operator_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        operator_label.setFixedSize(width, 50)
        return operator_label
