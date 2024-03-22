from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from ui_sidebar import Ui_MainWindow
from database import Data


class StoragePage (QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.conn = Data()

        self.btn_add_new_position.clicked.connect(test_change)

        def test_change():
            pass


    

