from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_sidebar import Ui_MainWindow


class SideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Zalupa")

        self.icon_name_widget.setHidden(True)
        self.stackedWidget.setCurrentIndex(0)

        self.home_1.clicked.connect(self.switch_to_homePage)
        self.home_2.clicked.connect(self.switch_to_homePage)
        self.home_1.setChecked(True)

        self.storage_1.clicked.connect(self.switch_to_storagePage)
        self.storage_2.clicked.connect(self.switch_to_storagePage)

        self.comming_1_1.clicked.connect(self.switch_to_comm1Page)
        self.comming_1_2.clicked.connect(self.switch_to_comm1Page)

        self.comming_2_1.clicked.connect(self.switch_to_comm2Page)
        self.comming_2_2.clicked.connect(self.switch_to_comm2Page)

        self.comming_3_1.clicked.connect(self.switch_to_comm3Page)
        self.comming_3_2.clicked.connect(self.switch_to_comm3Page)

    def switch_to_homePage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_storagePage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_comm1Page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_comm2Page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_comm3Page(self):
        self.stackedWidget.setCurrentIndex(4)