# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_position.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(491, 562)
        Dialog.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 471, 541))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_article = QLineEdit(self.widget)
        self.line_article.setObjectName(u"line_article")

        self.verticalLayout.addWidget(self.line_article)

        self.line_quantity = QLineEdit(self.widget)
        self.line_quantity.setObjectName(u"line_quantity")

        self.verticalLayout.addWidget(self.line_quantity)

        self.line_price = QLineEdit(self.widget)
        self.line_price.setObjectName(u"line_price")

        self.verticalLayout.addWidget(self.line_price)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ok = QPushButton(self.widget)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(30, 25))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.btn_ok.setFont(font)
        self.btn_ok.setStyleSheet(u"border: 1px solid #000000;\n"
"border-radius: 5px;")
        self.btn_ok.setCheckable(True)
        self.btn_ok.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(self.widget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(30, 25))
        self.btn_cancel.setStyleSheet(u"border: 1px solid #000000;\n"
"border-radius: 5px;")
        self.btn_cancel.setCheckable(True)
        self.btn_cancel.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(whatsthis)
        self.widget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.widget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.widget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

