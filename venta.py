import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []
    def data(self, index, role):
        if role == Qt.DisplayRole:
        status, text = self.todos[index.row()]
        return text
    def rowCount(self, index):
        return len(self.todos)