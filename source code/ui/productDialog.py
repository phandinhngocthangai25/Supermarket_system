# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.txtName = QLineEdit(Dialog)
        self.txtName.setObjectName(u"txtName")

        self.gridLayout.addWidget(self.txtName, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.txtQuantity = QLineEdit(Dialog)
        self.txtQuantity.setObjectName(u"txtQuantity")

        self.gridLayout.addWidget(self.txtQuantity, 1, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.txtCostPrice = QLineEdit(Dialog)
        self.txtCostPrice.setObjectName(u"txtCostPrice")

        self.gridLayout.addWidget(self.txtCostPrice, 2, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.txtSellingPrice = QLineEdit(Dialog)
        self.txtSellingPrice.setObjectName(u"txtSellingPrice")

        self.gridLayout.addWidget(self.txtSellingPrice, 3, 1, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.txtUnit = QLineEdit(Dialog)
        self.txtUnit.setObjectName(u"txtUnit")

        self.gridLayout.addWidget(self.txtUnit, 4, 1, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.txTexpiryDate = QLineEdit(Dialog)
        self.txTexpiryDate.setObjectName(u"txTexpiryDate")

        self.gridLayout.addWidget(self.txTexpiryDate, 5, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"T\u00ean s\u1ea3n ph\u1ea9m", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Gi\u00e1 nh\u1eadp", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Gi\u00e1 b\u00e1n", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0110\u01a1n v\u1ecb", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"H\u1ea1n s\u1eed d\u1ee5ng", None))
    # retranslateUi

