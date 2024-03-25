from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from ui_sidebar import Ui_MainWindow
from ui_new_position import Ui_Dialog


class SideBar(QMainWindow, Ui_MainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Zalupa")

        self.icon_name_widget.setHidden(True)
        self.stackedWidget.setCurrentIndex(0)

        self.home_1.clicked.connect(self.switch_to_homePage)
        self.home_2.clicked.connect(self.switch_to_homePage)
        self.home_1.setChecked(True)

        self.btn_add_new_position.clicked.connect(self.open_new_position_window)


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
        

    def open_new_position_window(self):
            self.show_window = self.setupUi(MainWindow=Ui_Dialog)