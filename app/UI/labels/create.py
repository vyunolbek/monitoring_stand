from PyQt6.QtWidgets import *
from UI.labels.design import DesignLabels as ld


class Labels(object):

    def __init__(self, operator: str):
        self.text_operator = operator


    def operator_label(self) -> QLabel:
        """Operator label design"""
        operator_label = QLabel(f"Operator: {self.text_operator}")
        operator_label = ld.operator_label(operator_label)
        return operator_label
