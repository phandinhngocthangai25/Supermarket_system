# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employeeManager.ui'
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

class Ui_employee(object):
    def setupUi(self, employee):
        if not employee.objectName():
            employee.setObjectName(u"employee")
        employee.resize(936, 615)
        self.verticalLayout = QVBoxLayout(employee)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(employee)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtSearchEmployee = QLineEdit(self.frame)
        self.txtSearchEmployee.setObjectName(u"txtSearchEmployee")

        self.horizontalLayout.addWidget(self.txtSearchEmployee)

        self.btnSearchEmployee = QPushButton(self.frame)
        self.btnSearchEmployee.setObjectName(u"btnSearchEmployee")

        self.horizontalLayout.addWidget(self.btnSearchEmployee)

        self.btnAddEmployee = QPushButton(self.frame)
        self.btnAddEmployee.setObjectName(u"btnAddEmployee")

        self.horizontalLayout.addWidget(self.btnAddEmployee)

        self.btnEditEmployee = QPushButton(self.frame)
        self.btnEditEmployee.setObjectName(u"btnEditEmployee")

        self.horizontalLayout.addWidget(self.btnEditEmployee)


        self.verticalLayout.addWidget(self.frame)

        self.scrollContainer = QScrollArea(employee)
        self.scrollContainer.setObjectName(u"scrollContainer")
        self.scrollContainer.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 914, 537))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableEmployee = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableEmployee.columnCount() < 9):
            self.tableEmployee.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableEmployee.setObjectName(u"tableEmployee")

        self.horizontalLayout_2.addWidget(self.tableEmployee)

        self.scrollContainer.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollContainer)


        self.retranslateUi(employee)

        QMetaObject.connectSlotsByName(employee)
    # setupUi

    def retranslateUi(self, employee):
        employee.setWindowTitle(QCoreApplication.translate("employee", u"Form", None))
        self.txtSearchEmployee.setPlaceholderText(QCoreApplication.translate("employee", u"T\u00ecm ki\u1ebfm nh\u00e2n vi\u00ean", None))
        self.btnSearchEmployee.setText(QCoreApplication.translate("employee", u"T\u00ecm ki\u1ebfm", None))
        self.btnAddEmployee.setText(QCoreApplication.translate("employee", u"Th\u00eam m\u1edbi nh\u00e2n vi\u00ean", None))
        self.btnEditEmployee.setText(QCoreApplication.translate("employee", u"s\u1eeda", None))
        ___qtablewidgetitem = self.tableEmployee.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("employee", u"M\u00e3 nh\u00e2n vi\u00ean", None))
        ___qtablewidgetitem1 = self.tableEmployee.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("employee", u"T\u00ean nh\u00e2n vi\u00ean", None))
        ___qtablewidgetitem2 = self.tableEmployee.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("employee", u"T\u00ean t\u00e0i kho\u1ea3n", None))
        ___qtablewidgetitem3 = self.tableEmployee.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("employee", u"M\u1eadt kh\u1ea9u", None))
        ___qtablewidgetitem4 = self.tableEmployee.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("employee", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        ___qtablewidgetitem5 = self.tableEmployee.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("employee", u"Email", None))
        ___qtablewidgetitem6 = self.tableEmployee.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("employee", u"\u0110\u1ecba ch\u1ec9", None))
        ___qtablewidgetitem7 = self.tableEmployee.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("employee", u"L\u01b0\u01a1ng", None))
        ___qtablewidgetitem8 = self.tableEmployee.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("employee", u"vai tr\u00f2", None))
    # retranslateUi

