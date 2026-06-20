# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'winUser.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_winUser(object):
    def setupUi(self, winUser):
        if not winUser.objectName():
            winUser.setObjectName(u"winUser")
        winUser.resize(1112, 688)
        self.centralwidget = QWidget(winUser)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* ---- TO\u00c0N B\u1ed8 C\u1eecA S\u1ed4 ---- */\n"
"QMainWindow {\n"
"    background-color: #121212; /* N\u1ec1n t\u1ed1i t\u1ed5ng th\u1ec3 */\n"
"}\n"
"\n"
"/* ---- THANH SIDEBAR B\u00caN TR\u00c1I ---- */\n"
"QFrame#frameSidebar {\n"
"    background-color: #1e1e1e; /* M\u00e0u n\u1ec1n Sidebar s\u00e1ng h\u01a1n n\u1ec1n ch\u00ednh m\u1ed9t ch\u00fat */\n"
"    border-right: 1px solid #2d2d2d; /* \u0110\u01b0\u1eddng chia c\u1eaft d\u1ecdc m\u1edd */\n"
"}\n"
"\n"
"/* ---- C\u00c1C N\u00daT B\u1ea4M TR\u00caN SIDEBAR ---- */\n"
"QFrame#frameSidebar QPushButton {\n"
"    background-color: transparent; /* X\u00f3a n\u1ec1n x\u00e1m th\u00f4 c\u1ee7a n\u00fat m\u1eb7c \u0111\u1ecbnh */\n"
"    color: #b3b3b3; /* M\u00e0u ch\u1eef x\u00e1m nh\u1eb9 */\n"
"    border: none; /* X\u00f3a vi\u1ec1n n\u00fat */\n"
"    border-radius: 6px; /* Bo g\u00f3c nh\u1eb9 cho n\u00fat */\n"
"    text-align: left; /* C\u0103n ch\u1eef sang b\u00ean tr\u00e1i */\n"
"    padding-left: 15px; /* \u0110\u1ea9y ch\u1eef c\u00e1ch"
                        " m\u00e9p tr\u00e1i ra m\u1ed9t ch\u00fat */\n"
"    height: 42px; /* C\u1ed1 \u0111\u1ecbnh chi\u1ec1u cao c\u00e1c n\u00fat cho \u0111\u1ec1u nhau */\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi r\u00ea chu\u1ed9t v\u00e0o c\u00e1c n\u00fat menu */\n"
"QFrame#frameSidebar QPushButton:hover {\n"
"    background-color: #2a2a2a; /* N\u1ec1n s\u00e1ng l\u00ean */\n"
"    color: #ffffff; /* Ch\u1eef chuy\u1ec3n sang m\u00e0u tr\u1eafng */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng ri\u00eang d\u00e0nh cho n\u00fat \u0110\u0103ng Xu\u1ea5t n\u1eb1m d\u01b0\u1edbi c\u00f9ng */\n"
"QFrame#frameSidebar QPushButton#btnDangXuat {\n"
"    color: #ff5555; /* Ch\u1eef m\u00e0u \u0111\u1ecf \u0111\u1ec3 c\u1ea3nh b\u00e1o */\n"
"}\n"
"QFrame#frameSidebar QPushButton#btnDangXuat:hover {\n"
"    background-color: #3a1a1a; /* N\u1ec1n \u0111\u1ecf t\u1ed1i khi hover */\n"
"    color: #ff6e6e;\n"
"}\n"
"\n"
"/* ---- V\u00d9NG N\u1ed8I DUNG B\u00caN PH\u1ea2I ---- */\n"
"QStackedWidget#"
                        "stackedContent {\n"
"    background-color: #181818; /* N\u1ec1n c\u1ee7a v\u00f9ng hi\u1ec3n th\u1ecb n\u1ed9i dung */\n"
"    border-radius: 8px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameSidebar = QFrame(self.centralwidget)
        self.frameSidebar.setObjectName(u"frameSidebar")
        self.frameSidebar.setMaximumSize(QSize(200, 16777215))
        self.frameSidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameSidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frameSidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnPayment = QPushButton(self.frameSidebar)
        self.btnPayment.setObjectName(u"btnPayment")
        self.btnPayment.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btnPayment)

        self.btnHistory = QPushButton(self.frameSidebar)
        self.btnHistory.setObjectName(u"btnHistory")
        self.btnHistory.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btnHistory)

        self.btnProduct = QPushButton(self.frameSidebar)
        self.btnProduct.setObjectName(u"btnProduct")
        self.btnProduct.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btnProduct)

        self.btnCustomer = QPushButton(self.frameSidebar)
        self.btnCustomer.setObjectName(u"btnCustomer")
        self.btnCustomer.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btnCustomer)

        self.btnEmployee = QPushButton(self.frameSidebar)
        self.btnEmployee.setObjectName(u"btnEmployee")
        self.btnEmployee.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btnEmployee)

        self.verticalSpacer = QSpacerItem(20, 170, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnLogout = QPushButton(self.frameSidebar)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.btnLogout)


        self.horizontalLayout.addWidget(self.frameSidebar)

        self.stackedContent = QStackedWidget(self.centralwidget)
        self.stackedContent.setObjectName(u"stackedContent")

        self.horizontalLayout.addWidget(self.stackedContent)

        winUser.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(winUser)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1112, 33))
        winUser.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(winUser)
        self.statusbar.setObjectName(u"statusbar")
        winUser.setStatusBar(self.statusbar)

        self.retranslateUi(winUser)

        self.stackedContent.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(winUser)
    # setupUi

    def retranslateUi(self, winUser):
        winUser.setWindowTitle(QCoreApplication.translate("winUser", u"MainWindow", None))
        self.btnPayment.setText(QCoreApplication.translate("winUser", u"Thanh to\u00e1n", None))
        self.btnHistory.setText(QCoreApplication.translate("winUser", u"L\u1ecbch s\u1eed h\u00f3a \u0111\u01a1n", None))
        self.btnProduct.setText(QCoreApplication.translate("winUser", u"H\u00e0ng h\u00f3a", None))
        self.btnCustomer.setText(QCoreApplication.translate("winUser", u"Qu\u1ea3n l\u00fd kh\u00e1ch h\u00e0ng", None))
        self.btnEmployee.setText(QCoreApplication.translate("winUser", u"Qu\u1ea3n l\u00fd nh\u00e2n vi\u00ean", None))
        self.btnLogout.setText(QCoreApplication.translate("winUser", u"\u0110\u0103ng xu\u1ea5t", None))
    # retranslateUi

