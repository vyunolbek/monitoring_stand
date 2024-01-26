from PyQt6.QtWidgets import *
from UI.labels.design import DesignLabels as ld


class Labels(object):

    def __init__(self, operator: str, width: int):
        self.text_operator = operator
        self.width = width


    def operator_label(self) -> QLabel:
        """Operator label create"""
        operator_label = QLabel(f"Operator: {self.text_operator}")
        ld.operator_label(operator_label, self.width)
        return operator_label
