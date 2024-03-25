from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6 import QtWidgets
import sys
from sidebar import SideBar
from ui_sidebar import Ui_MainWindow
from ui_new_position import Ui_Dialog


class StorageSys(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(StorageSys, self).__init__()

        self.ui = SideBar()
        self.ui.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StorageSys()
    app.exec()