# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productManager.ui'
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

class Ui_product(object):
    def setupUi(self, product):
        if not product.objectName():
            product.setObjectName(u"product")
        product.resize(926, 558)
        self.verticalLayout = QVBoxLayout(product)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(product)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtSearchProduct = QLineEdit(self.frame)
        self.txtSearchProduct.setObjectName(u"txtSearchProduct")

        self.horizontalLayout.addWidget(self.txtSearchProduct)

        self.btnSearch = QPushButton(self.frame)
        self.btnSearch.setObjectName(u"btnSearch")

        self.horizontalLayout.addWidget(self.btnSearch)

        self.btnAddProduct = QPushButton(self.frame)
        self.btnAddProduct.setObjectName(u"btnAddProduct")

        self.horizontalLayout.addWidget(self.btnAddProduct)

        self.btnEditProduct = QPushButton(self.frame)
        self.btnEditProduct.setObjectName(u"btnEditProduct")

        self.horizontalLayout.addWidget(self.btnEditProduct)


        self.verticalLayout.addWidget(self.frame)

        self.scrollContainer = QScrollArea(product)
        self.scrollContainer.setObjectName(u"scrollContainer")
        self.scrollContainer.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 904, 482))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableProduct = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableProduct.columnCount() < 7):
            self.tableProduct.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableProduct.setObjectName(u"tableProduct")
        self.tableProduct.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_2.addWidget(self.tableProduct)

        self.scrollContainer.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollContainer)


        self.retranslateUi(product)

        QMetaObject.connectSlotsByName(product)
    # setupUi

    def retranslateUi(self, product):
        product.setWindowTitle(QCoreApplication.translate("product", u"Form", None))
        self.txtSearchProduct.setPlaceholderText(QCoreApplication.translate("product", u"T\u00ecm s\u1ea3n ph\u1ea9m", None))
        self.btnSearch.setText(QCoreApplication.translate("product", u"T\u00ecm ki\u1ebfm", None))
        self.btnAddProduct.setText(QCoreApplication.translate("product", u"Th\u00eam m\u1edbi", None))
        self.btnEditProduct.setText(QCoreApplication.translate("product", u"S\u1eeda", None))
        ___qtablewidgetitem = self.tableProduct.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("product", u"M\u00e3 s\u1ea3n ph\u1ea9m", None))
        ___qtablewidgetitem1 = self.tableProduct.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("product", u"T\u00ean s\u1ea3n ph\u1ea9m", None))
        ___qtablewidgetitem2 = self.tableProduct.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("product", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        ___qtablewidgetitem3 = self.tableProduct.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("product", u"Gi\u00e1 nh\u1eadp", None))
        ___qtablewidgetitem4 = self.tableProduct.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("product", u"Gi\u00e1 b\u00e1n", None))
        ___qtablewidgetitem5 = self.tableProduct.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("product", u"\u0110\u01a1n v\u1ecb", None))
        ___qtablewidgetitem6 = self.tableProduct.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("product", u"H\u1ea1n s\u1eed d\u1ee5ng", None))
    # retranslateUi

