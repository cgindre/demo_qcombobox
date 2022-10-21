# -*- coding: utf-8 -*-

import sys
from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import *


class tab_temps(QDialog):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.table = QtWidgets.QTableWidget(3, 2)
        #self.setCentralWidget(self.label)

def on_activated():
    print("on_activated")

def on_current_text_changed():
    print("current_text_changed")

def on_edit_text_changed():
    print("edit_text_changed")

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    qd = QDialog()
    qd.setWindowTitle("Petit exemple !")
    lyt = QVBoxLayout()

    label = QLabel("Demo QComboBox")
    cbb = QComboBox()
    items_grandeurs = ["Activité", "Activité volumique", "Masse", "Atomes"]
    cbb.currentTextChanged.connect(on_current_text_changed)
    cbb.editTextChanged.connect(on_edit_text_changed)
    cbb.activated.connect(on_activated)

    cbb.addItems(items_grandeurs)
    cbb.setCurrentText(items_grandeurs[0])

    lyt.addWidget(label)
    lyt.addWidget(cbb)
    qd.setLayout(lyt)
    qd.show()
    app.exec()
