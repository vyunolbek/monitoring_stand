from PyQt6.QtWidgets import *


class DesignLabels(object):

    @staticmethod
    def operator_label(operator_label: QLabel) -> QLabel:
        operator_label.setStyleSheet("font-size: 20px; color: black;")
        operator_label.setFixedHeight(40)
        return operator_label
