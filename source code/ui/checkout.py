# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'checkout.ui'
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
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_chechout(object):
    def setupUi(self, chechout):
        if not chechout.objectName():
            chechout.setObjectName(u"chechout")
        chechout.resize(927, 557)
        self.horizontalLayout = QHBoxLayout(chechout)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameCart = QFrame(chechout)
        self.frameCart.setObjectName(u"frameCart")
        self.frameCart.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameCart.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameCart)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.frameCart)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.txtSearchProduct = QLineEdit(self.frame)
        self.txtSearchProduct.setObjectName(u"txtSearchProduct")

        self.horizontalLayout_4.addWidget(self.txtSearchProduct)

        self.btnAddProduct = QPushButton(self.frame)
        self.btnAddProduct.setObjectName(u"btnAddProduct")

        self.horizontalLayout_4.addWidget(self.btnAddProduct)


        self.verticalLayout_4.addWidget(self.frame)

        self.scrollCartContainer = QScrollArea(self.frameCart)
        self.scrollCartContainer.setObjectName(u"scrollCartContainer")
        self.scrollCartContainer.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 627, 459))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableCartItems = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableCartItems.columnCount() < 6):
            self.tableCartItems.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCartItems.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCartItems.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCartItems.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCartItems.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableCartItems.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableCartItems.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableCartItems.setObjectName(u"tableCartItems")
        self.tableCartItems.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.tableCartItems)

        self.scrollCartContainer.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollCartContainer)


        self.horizontalLayout.addWidget(self.frameCart)

        self.frameCheckout = QFrame(chechout)
        self.frameCheckout.setObjectName(u"frameCheckout")
        self.frameCheckout.setMaximumSize(QSize(250, 16777215))
        self.frameCheckout.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameCheckout.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameCheckout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txtSearchCustomer = QLineEdit(self.frameCheckout)
        self.txtSearchCustomer.setObjectName(u"txtSearchCustomer")
        self.txtSearchCustomer.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.txtSearchCustomer)

        self.txtDiscount = QLineEdit(self.frameCheckout)
        self.txtDiscount.setObjectName(u"txtDiscount")
        self.txtDiscount.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.txtDiscount)

        self.frame_3 = QFrame(self.frameCheckout)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.txtFinalAmount = QLabel(self.frame_3)
        self.txtFinalAmount.setObjectName(u"txtFinalAmount")
        self.txtFinalAmount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.txtFinalAmount)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pushButton_3 = QPushButton(self.frameCheckout)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.frameCheckout)


        self.retranslateUi(chechout)

        QMetaObject.connectSlotsByName(chechout)
    # setupUi

    def retranslateUi(self, chechout):
        chechout.setWindowTitle(QCoreApplication.translate("chechout", u"Form", None))
        self.txtSearchProduct.setPlaceholderText(QCoreApplication.translate("chechout", u"T\u00ecm ki\u1ebfm h\u00e0ng h\u00f3a", None))
        self.btnAddProduct.setText(QCoreApplication.translate("chechout", u"+", None))
        ___qtablewidgetitem = self.tableCartItems.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("chechout", u"STT", None))
        ___qtablewidgetitem1 = self.tableCartItems.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("chechout", u"T\u00ean s\u1ea3n ph\u1ea9m", None))
        ___qtablewidgetitem2 = self.tableCartItems.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("chechout", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        ___qtablewidgetitem3 = self.tableCartItems.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("chechout", u"\u0110\u01a1n gi\u00e1", None))
        ___qtablewidgetitem4 = self.tableCartItems.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("chechout", u"Th\u00e0nh ti\u1ec1n", None))
        ___qtablewidgetitem5 = self.tableCartItems.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("chechout", u"X\u00f3a", None))
        self.txtSearchCustomer.setPlaceholderText(QCoreApplication.translate("chechout", u"T\u00ecm kh\u00e1ch h\u00e0ng", None))
        self.txtDiscount.setPlaceholderText(QCoreApplication.translate("chechout", u"S\u1ed1 ti\u1ec1n gi\u1ea3m gi\u00e1", None))
        self.label.setText(QCoreApplication.translate("chechout", u"S\u1ed1 ti\u1ec1n thanh to\u00e1n", None))
        self.txtFinalAmount.setText(QCoreApplication.translate("chechout", u"0", None))
        self.pushButton_3.setText(QCoreApplication.translate("chechout", u"Thanh to\u00e1n", None))
    # retranslateUi

