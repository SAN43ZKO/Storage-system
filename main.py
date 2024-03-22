from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys
from sidebar import SideBar

app = QApplication(sys.argv)

window = SideBar()


window.show()
app.exec()