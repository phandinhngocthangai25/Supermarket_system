# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customerManager.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_customer(object):
    def setupUi(self, customer):
        if not customer.objectName():
            customer.setObjectName(u"customer")
        customer.resize(716, 459)
        self.verticalLayout = QVBoxLayout(customer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(customer)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtSearchCustomer = QLineEdit(self.frame)
        self.txtSearchCustomer.setObjectName(u"txtSearchCustomer")

        self.horizontalLayout.addWidget(self.txtSearchCustomer)

        self.btnSearchCustomer = QPushButton(self.frame)
        self.btnSearchCustomer.setObjectName(u"btnSearchCustomer")

        self.horizontalLayout.addWidget(self.btnSearchCustomer)

        self.btnAddCustomer = QPushButton(self.frame)
        self.btnAddCustomer.setObjectName(u"btnAddCustomer")

        self.horizontalLayout.addWidget(self.btnAddCustomer)

        self.btnEditCustomer = QPushButton(self.frame)
        self.btnEditCustomer.setObjectName(u"btnEditCustomer")

        self.horizontalLayout.addWidget(self.btnEditCustomer)


        self.verticalLayout.addWidget(self.frame)

        self.scrollContainer = QScrollArea(customer)
        self.scrollContainer.setObjectName(u"scrollContainer")
        self.scrollContainer.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 694, 381))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableCustomer = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableCustomer.columnCount() < 6):
            self.tableCustomer.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCustomer.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCustomer.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCustomer.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCustomer.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableCustomer.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableCustomer.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableCustomer.setObjectName(u"tableCustomer")

        self.horizontalLayout_2.addWidget(self.tableCustomer)

        self.scrollContainer.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollContainer)


        self.retranslateUi(customer)

        QMetaObject.connectSlotsByName(customer)
    # setupUi

    def retranslateUi(self, customer):
        customer.setWindowTitle(QCoreApplication.translate("customer", u"Form", None))
        self.txtSearchCustomer.setPlaceholderText(QCoreApplication.translate("customer", u"T\u00ecm ki\u1ebfm kh\u00e1ch h\u00e0ng", None))
        self.btnSearchCustomer.setText(QCoreApplication.translate("customer", u"T\u00ecm ki\u1ebfm", None))
        self.btnAddCustomer.setText(QCoreApplication.translate("customer", u"Th\u00eam m\u1edbi kh\u00e1ch h\u00e0ng", None))
        self.btnEditCustomer.setText(QCoreApplication.translate("customer", u"S\u1eeda ", None))
        ___qtablewidgetitem = self.tableCustomer.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("customer", u"M\u00e3 kh\u00e1ch h\u00e0ng", None))
        ___qtablewidgetitem1 = self.tableCustomer.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("customer", u"T\u00ean kh\u00e1ch h\u00e0ng", None))
        ___qtablewidgetitem2 = self.tableCustomer.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("customer", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        ___qtablewidgetitem3 = self.tableCustomer.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("customer", u"Email", None))
        ___qtablewidgetitem4 = self.tableCustomer.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("customer", u"\u0110\u1ecba ch\u1ec9", None))
        ___qtablewidgetitem5 = self.tableCustomer.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("customer", u"\u0110i\u1ec3m th\u01b0\u1edfng", None))
    # retranslateUi

