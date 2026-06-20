# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoiceHistory.ui'
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

class Ui_invoice(object):
    def setupUi(self, invoice):
        if not invoice.objectName():
            invoice.setObjectName(u"invoice")
        invoice.resize(926, 560)
        self.verticalLayout = QVBoxLayout(invoice)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameSearch = QFrame(invoice)
        self.frameSearch.setObjectName(u"frameSearch")
        self.frameSearch.setMaximumSize(QSize(16777215, 50))
        self.frameSearch.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameSearch.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frameSearch)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txtSearch = QLineEdit(self.frameSearch)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout_5.addWidget(self.txtSearch)

        self.btnSearch = QPushButton(self.frameSearch)
        self.btnSearch.setObjectName(u"btnSearch")

        self.horizontalLayout_5.addWidget(self.btnSearch)


        self.verticalLayout.addWidget(self.frameSearch)

        self.scrollArea = QScrollArea(invoice)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 904, 484))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableInvoice = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableInvoice.columnCount() < 5):
            self.tableInvoice.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableInvoice.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableInvoice.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableInvoice.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableInvoice.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableInvoice.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableInvoice.setObjectName(u"tableInvoice")
        self.tableInvoice.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.tableInvoice)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(invoice)

        QMetaObject.connectSlotsByName(invoice)
    # setupUi

    def retranslateUi(self, invoice):
        invoice.setWindowTitle(QCoreApplication.translate("invoice", u"Form", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("invoice", u"T\u00ecm ki\u1ebfm h\u00f3a \u0111\u01a1n", None))
        self.btnSearch.setText(QCoreApplication.translate("invoice", u"T\u00ecm", None))
        ___qtablewidgetitem = self.tableInvoice.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("invoice", u"M\u00e3 h\u00f3a \u0111\u01a1n", None))
        ___qtablewidgetitem1 = self.tableInvoice.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("invoice", u"T\u00ean kh\u00e1ch h\u00e0ng", None))
        ___qtablewidgetitem2 = self.tableInvoice.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("invoice", u"T\u00ean nh\u00e2n vi\u00ean", None))
        ___qtablewidgetitem3 = self.tableInvoice.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("invoice", u"T\u1ed5ng ti\u1ec1n thanh to\u00e1n", None))
        ___qtablewidgetitem4 = self.tableInvoice.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("invoice", u"Ng\u00e0y thanh to\u00e1n", None))
    # retranslateUi

