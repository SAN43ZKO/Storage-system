# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1117, 725)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.appbar_widget = QWidget(self.main_menu)
        self.appbar_widget.setObjectName(u"appbar_widget")
        self.appbar_widget.setStyleSheet(u"background-color: rgb(31, 149, 239);")
        self.horizontalLayout_4 = QHBoxLayout(self.appbar_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.menu = QPushButton(self.appbar_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/image/menu_lines_hamburger_icon_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon)
        self.menu.setIconSize(QSize(30, 30))
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(468, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.appbar_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(150, 0))
        self.lineEdit.setMaximumSize(QSize(150, 16777215))
        self.lineEdit.setStyleSheet(u"border-radius:10px;\n"
"border: 1px solid #e0e4e7;")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_13 = QPushButton(self.appbar_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/image/search_zoom_icon_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pushButton_13)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.appbar_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.label_4 = QLabel(self.home_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 250, 121, 91))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_4.setFont(font)
        self.stackedWidget.addWidget(self.home_page)
        self.storage_page = QWidget()
        self.storage_page.setObjectName(u"storage_page")
        self.verticalLayout_6 = QVBoxLayout(self.storage_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.storage_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.btn_add_new_position = QPushButton(self.storage_page)
        self.btn_add_new_position.setObjectName(u"btn_add_new_position")
        self.btn_add_new_position.setMaximumSize(QSize(60, 60))
        self.btn_add_new_position.setStyleSheet(u"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/image/plus_round_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_new_position.setIcon(icon2)
        self.btn_add_new_position.setIconSize(QSize(30, 30))
        self.btn_add_new_position.setCheckable(True)
        self.btn_add_new_position.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.btn_add_new_position)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.tableView = QTableView(self.storage_page)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_6.addWidget(self.tableView)

        self.stackedWidget.addWidget(self.storage_page)
        self.comm1_page = QWidget()
        self.comm1_page.setObjectName(u"comm1_page")
        self.label_6 = QLabel(self.comm1_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 240, 391, 51))
        self.label_6.setFont(font)
        self.stackedWidget.addWidget(self.comm1_page)
        self.comm2_page = QWidget()
        self.comm2_page.setObjectName(u"comm2_page")
        self.label_7 = QLabel(self.comm2_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 270, 391, 51))
        self.label_7.setFont(font)
        self.stackedWidget.addWidget(self.comm2_page)
        self.comm3_page = QWidget()
        self.comm3_page.setObjectName(u"comm3_page")
        self.label_8 = QLabel(self.comm3_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 260, 391, 51))
        self.label_8.setFont(font)
        self.stackedWidget.addWidget(self.comm3_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:#f5fafe;\n"
"	color:#1f95ef;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 11, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/image/1491580635-yumminkysocialmedia26_83102.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(17)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.home_1 = QPushButton(self.icon_only_widget)
        self.home_1.setObjectName(u"home_1")
        icon3 = QIcon()
        icon3.addFile(u":/image/home_icon_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/image/home_icon_black.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_1.setIcon(icon3)
        self.home_1.setIconSize(QSize(35, 35))
        self.home_1.setCheckable(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_1)

        self.storage_1 = QPushButton(self.icon_only_widget)
        self.storage_1.setObjectName(u"storage_1")
        icon4 = QIcon()
        icon4.addFile(u":/image/storage_icon_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/image/storage_icon_black.svg", QSize(), QIcon.Normal, QIcon.On)
        self.storage_1.setIcon(icon4)
        self.storage_1.setIconSize(QSize(35, 35))
        self.storage_1.setCheckable(True)
        self.storage_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.storage_1)

        self.comming_1_1 = QPushButton(self.icon_only_widget)
        self.comming_1_1.setObjectName(u"comming_1_1")
        icon5 = QIcon()
        icon5.addFile(u":/image/star_icon_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/image/star_icon_black.svg", QSize(), QIcon.Normal, QIcon.On)
        self.comming_1_1.setIcon(icon5)
        self.comming_1_1.setIconSize(QSize(35, 35))
        self.comming_1_1.setCheckable(True)
        self.comming_1_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.comming_1_1)

        self.comming_2_1 = QPushButton(self.icon_only_widget)
        self.comming_2_1.setObjectName(u"comming_2_1")
        self.comming_2_1.setIcon(icon5)
        self.comming_2_1.setIconSize(QSize(35, 35))
        self.comming_2_1.setCheckable(True)
        self.comming_2_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.comming_2_1)

        self.comming_3_1 = QPushButton(self.icon_only_widget)
        self.comming_3_1.setObjectName(u"comming_3_1")
        self.comming_3_1.setIcon(icon5)
        self.comming_3_1.setIconSize(QSize(35, 35))
        self.comming_3_1.setCheckable(True)
        self.comming_3_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.comming_3_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 373, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.theme_btn = QPushButton(self.icon_only_widget)
        self.theme_btn.setObjectName(u"theme_btn")
        icon6 = QIcon()
        icon6.addFile(u":/image/sunny_icon_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/image/moon_icon_black.svg", QSize(), QIcon.Normal, QIcon.On)
        self.theme_btn.setIcon(icon6)
        self.theme_btn.setIconSize(QSize(35, 35))
        self.theme_btn.setCheckable(True)
        self.theme_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.theme_btn)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:#f5fafe;\n"
"	color:#1f95ef;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/image/1491580635-yumminkysocialmedia26_83102.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(17)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.home_2 = QPushButton(self.icon_name_widget)
        self.home_2.setObjectName(u"home_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.home_2.setFont(font2)
        self.home_2.setIcon(icon3)
        self.home_2.setIconSize(QSize(35, 35))
        self.home_2.setCheckable(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_2)

        self.storage_2 = QPushButton(self.icon_name_widget)
        self.storage_2.setObjectName(u"storage_2")
        self.storage_2.setFont(font2)
        self.storage_2.setIcon(icon4)
        self.storage_2.setIconSize(QSize(35, 35))
        self.storage_2.setCheckable(True)
        self.storage_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.storage_2)

        self.comming_1_2 = QPushButton(self.icon_name_widget)
        self.comming_1_2.setObjectName(u"comming_1_2")
        self.comming_1_2.setFont(font2)
        self.comming_1_2.setIcon(icon5)
        self.comming_1_2.setIconSize(QSize(35, 35))
        self.comming_1_2.setCheckable(True)
        self.comming_1_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.comming_1_2)

        self.comming_2_2 = QPushButton(self.icon_name_widget)
        self.comming_2_2.setObjectName(u"comming_2_2")
        self.comming_2_2.setFont(font2)
        self.comming_2_2.setIcon(icon5)
        self.comming_2_2.setIconSize(QSize(35, 35))
        self.comming_2_2.setCheckable(True)
        self.comming_2_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.comming_2_2)

        self.comming_3_2 = QPushButton(self.icon_name_widget)
        self.comming_3_2.setObjectName(u"comming_3_2")
        self.comming_3_2.setFont(font2)
        self.comming_3_2.setIcon(icon5)
        self.comming_3_2.setIconSize(QSize(35, 35))
        self.comming_3_2.setCheckable(True)
        self.comming_3_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.comming_3_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 373, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.theme_btn_2 = QPushButton(self.icon_name_widget)
        self.theme_btn_2.setObjectName(u"theme_btn_2")
        self.theme_btn_2.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/image/sunny_icon_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.theme_btn_2.setIcon(icon7)
        self.theme_btn_2.setIconSize(QSize(35, 35))
        self.theme_btn_2.setCheckable(True)
        self.theme_btn_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.theme_btn_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.comming_3_1.toggled.connect(self.comming_3_2.setChecked)
        self.comming_2_1.toggled.connect(self.comming_2_2.setChecked)
        self.comming_1_1.toggled.connect(self.comming_1_2.setChecked)
        self.storage_1.toggled.connect(self.storage_2.setChecked)
        self.home_1.toggled.connect(self.home_2.setChecked)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.storage_2.toggled.connect(self.storage_1.setChecked)
        self.comming_1_2.toggled.connect(self.comming_1_1.setChecked)
        self.comming_2_2.toggled.connect(self.comming_2_1.setChecked)
        self.comming_3_2.toggled.connect(self.comming_3_1.setChecked)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_13.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"STORAGE", None))
        self.btn_add_new_position.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"COMMING SOON_1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"COMMING SOON_2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"COMMING SOON_3", None))
        self.label.setText("")
        self.home_1.setText("")
        self.storage_1.setText("")
        self.comming_1_1.setText("")
        self.comming_2_1.setText("")
        self.comming_3_1.setText("")
        self.theme_btn.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SideBar", None))
        self.home_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.storage_2.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.comming_1_2.setText(QCoreApplication.translate("MainWindow", u"Comming1", None))
        self.comming_2_2.setText(QCoreApplication.translate("MainWindow", u"Comming2", None))
        self.comming_3_2.setText(QCoreApplication.translate("MainWindow", u"Comming3", None))
        self.theme_btn_2.setText(QCoreApplication.translate("MainWindow", u"Dark Theme", None))
    # retranslateUi

