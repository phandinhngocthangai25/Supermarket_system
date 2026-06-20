# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employeeDialog.ui'
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
        Dialog.resize(504, 458)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.txtRole = QLineEdit(Dialog)
        self.txtRole.setObjectName(u"txtRole")

        self.gridLayout.addWidget(self.txtRole, 12, 2, 1, 1)

        self.txtUserName = QLineEdit(Dialog)
        self.txtUserName.setObjectName(u"txtUserName")

        self.gridLayout.addWidget(self.txtUserName, 3, 2, 1, 1)

        self.txtEmployeeID = QLineEdit(Dialog)
        self.txtEmployeeID.setObjectName(u"txtEmployeeID")

        self.gridLayout.addWidget(self.txtEmployeeID, 0, 2, 1, 1)

        self.txtFullName = QLineEdit(Dialog)
        self.txtFullName.setObjectName(u"txtFullName")

        self.gridLayout.addWidget(self.txtFullName, 1, 2, 1, 1)

        self.txtPhone = QLineEdit(Dialog)
        self.txtPhone.setObjectName(u"txtPhone")

        self.gridLayout.addWidget(self.txtPhone, 8, 2, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 12, 0, 1, 1)

        self.txtPassword = QLineEdit(Dialog)
        self.txtPassword.setObjectName(u"txtPassword")

        self.gridLayout.addWidget(self.txtPassword, 5, 2, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 11, 0, 1, 1)

        self.txtSalary = QLineEdit(Dialog)
        self.txtSalary.setObjectName(u"txtSalary")

        self.gridLayout.addWidget(self.txtSalary, 11, 2, 1, 1)

        self.txtEmail = QLineEdit(Dialog)
        self.txtEmail.setObjectName(u"txtEmail")

        self.gridLayout.addWidget(self.txtEmail, 9, 2, 1, 1)

        self.txtAddress = QLineEdit(Dialog)
        self.txtAddress.setObjectName(u"txtAddress")

        self.gridLayout.addWidget(self.txtAddress, 10, 2, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"M\u1eadt kh\u1ea9u", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Vai tr\u00f2", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"T\u00ean nh\u00e2n vi\u00ean", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"M\u00e3 nh\u00e2n vi\u00ean", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"T\u00ean t\u00e0i kho\u1ea3n", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"L\u01b0\u01a1ng", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0110\u1ecba ch\u1ec9", None))
    # retranslateUi

