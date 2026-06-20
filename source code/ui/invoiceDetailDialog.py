# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoiceDetailDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QScrollArea, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(721, 549)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lblInvoiceID = QLabel(self.frame_2)
        self.lblInvoiceID.setObjectName(u"lblInvoiceID")

        self.horizontalLayout_2.addWidget(self.lblInvoiceID)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lblDateTime = QLabel(self.frame_2)
        self.lblDateTime.setObjectName(u"lblDateTime")

        self.horizontalLayout_2.addWidget(self.lblDateTime)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.lblEmployeeName = QLabel(self.frame_3)
        self.lblEmployeeName.setObjectName(u"lblEmployeeName")

        self.horizontalLayout.addWidget(self.lblEmployeeName)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.lblCustomerName = QLabel(self.frame_3)
        self.lblCustomerName.setObjectName(u"lblCustomerName")

        self.horizontalLayout.addWidget(self.lblCustomerName)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        self.scrollContainer = QScrollArea(Dialog)
        self.scrollContainer.setObjectName(u"scrollContainer")
        self.scrollContainer.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 699, 361))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableInvoiceDetail = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableInvoiceDetail.columnCount() < 4):
            self.tableInvoiceDetail.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableInvoiceDetail.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableInvoiceDetail.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableInvoiceDetail.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableInvoiceDetail.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableInvoiceDetail.setObjectName(u"tableInvoiceDetail")
        self.tableInvoiceDetail.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_4.addWidget(self.tableInvoiceDetail)

        self.scrollContainer.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollContainer)

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.lblTotalAmount = QLabel(self.frame_4)
        self.lblTotalAmount.setObjectName(u"lblTotalAmount")

        self.horizontalLayout_3.addWidget(self.lblTotalAmount)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.lblDiscount = QLabel(self.frame_4)
        self.lblDiscount.setObjectName(u"lblDiscount")

        self.horizontalLayout_3.addWidget(self.lblDiscount)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.lblFinalAmount = QLabel(self.frame_4)
        self.lblFinalAmount.setObjectName(u"lblFinalAmount")

        self.horizontalLayout_3.addWidget(self.lblFinalAmount)


        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"M\u00e3 h\u00f3a \u0111\u01a1n", None))
        self.lblInvoiceID.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Ng\u00e0y", None))
        self.lblDateTime.setText(QCoreApplication.translate("Dialog", u"01/01/1910", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"T\u00ean nh\u00e2n vi\u00ean", None))
        self.lblEmployeeName.setText(QCoreApplication.translate("Dialog", u"t\u00ean", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"T\u00ean kh\u00e1ch h\u00e0ng", None))
        self.lblCustomerName.setText(QCoreApplication.translate("Dialog", u"t\u00ean", None))
        ___qtablewidgetitem = self.tableInvoiceDetail.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"M\u1eb7t h\u00e0ng", None))
        ___qtablewidgetitem1 = self.tableInvoiceDetail.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        ___qtablewidgetitem2 = self.tableInvoiceDetail.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u0110\u01a1n gi\u00e1", None))
        ___qtablewidgetitem3 = self.tableInvoiceDetail.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"T\u1ed5ng", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"T\u1ed5ng ti\u1ec1n h\u00e0ng", None))
        self.lblTotalAmount.setText(QCoreApplication.translate("Dialog", u"ti\u1ec1n", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Khuy\u1ebfn m\u00e3i", None))
        self.lblDiscount.setText(QCoreApplication.translate("Dialog", u"ti\u1ec1n", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"T\u1ed5ng thanh to\u00e1n", None))
        self.lblFinalAmount.setText(QCoreApplication.translate("Dialog", u"ti\u1ec1n", None))
    # retranslateUi

