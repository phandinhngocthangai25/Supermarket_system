# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_winLogin(object):
    def setupUi(self, winLogin):
        if not winLogin.objectName():
            winLogin.setObjectName(u"winLogin")
        winLogin.resize(536, 354)
        self.centralwidget = QWidget(winLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frameLogin = QFrame(self.centralwidget)
        self.frameLogin.setObjectName(u"frameLogin")
        self.frameLogin.setGeometry(QRect(50, 10, 431, 271))
        self.frameLogin.setStyleSheet(u"/* \u00c1p d\u1ee5ng cho c\u00e1c \u00f4 nh\u1eadp li\u1ec7u */\n"
"QLineEdit {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #555555;\n"
"    border-radius: 6px; /* Bo g\u00f3c m\u1ec1m m\u1ea1i */\n"
"    padding: 6px 10px;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi ng\u01b0\u1eddi d\u00f9ng click v\u00e0o \u00f4 nh\u1eadp */\n"
"QLineEdit:focus {\n"
"    border: 1px solid #00a8ff; /* Vi\u1ec1n s\u00e1ng l\u00ean m\u00e0u xanh khi ch\u1ecdn */\n"
"}\n"
"\n"
"/* \u00c1p d\u1ee5ng cho n\u00fat \u0110\u0103ng Nh\u1eadp */\n"
"QPushButton {\n"
"    background-color: #00a8ff; /* \u0110\u1ed5i n\u00fat th\u00e0nh m\u00e0u xanh n\u1ed5i b\u1eadt */\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi di chu\u1ed9t v\u00e0o n\u00fat */\n"
"QPushButton:hover {\n"
"    background-color: #008cd1;\n"
"}")
        self.frameLogin.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLogin.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frameLogin)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lblTitle = QLabel(self.frameLogin)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.frame_3 = QFrame(self.frameLogin)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblUsername = QLabel(self.frame_3)
        self.lblUsername.setObjectName(u"lblUsername")

        self.horizontalLayout_2.addWidget(self.lblUsername)

        self.txtUsername = QLineEdit(self.frame_3)
        self.txtUsername.setObjectName(u"txtUsername")

        self.horizontalLayout_2.addWidget(self.txtUsername)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frameLogin)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblPassword = QLabel(self.frame_2)
        self.lblPassword.setObjectName(u"lblPassword")

        self.horizontalLayout.addWidget(self.lblPassword)

        self.txtPassword = QLineEdit(self.frame_2)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout.addWidget(self.txtPassword)


        self.verticalLayout.addWidget(self.frame_2)

        self.btnLogin = QPushButton(self.frameLogin)
        self.btnLogin.setObjectName(u"btnLogin")

        self.verticalLayout.addWidget(self.btnLogin)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        winLogin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(winLogin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 536, 33))
        winLogin.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(winLogin)
        self.statusbar.setObjectName(u"statusbar")
        winLogin.setStatusBar(self.statusbar)

        self.retranslateUi(winLogin)

        QMetaObject.connectSlotsByName(winLogin)
    # setupUi

    def retranslateUi(self, winLogin):
        winLogin.setWindowTitle(QCoreApplication.translate("winLogin", u"MainWindow", None))
        self.lblTitle.setText(QCoreApplication.translate("winLogin", u"\u0110\u0102NG NH\u1eacP", None))
        self.lblUsername.setText(QCoreApplication.translate("winLogin", u"T\u00ean \u0111\u0103ng nh\u1eadp", None))
        self.txtUsername.setPlaceholderText(QCoreApplication.translate("winLogin", u"Nh\u1eadp t\u00e0i kho\u1ea3n", None))
        self.lblPassword.setText(QCoreApplication.translate("winLogin", u"M\u1eadt kh\u1ea9u", None))
        self.txtPassword.setText("")
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("winLogin", u"Nh\u1eadp m\u1eadt kh\u1ea9u", None))
        self.btnLogin.setText(QCoreApplication.translate("winLogin", u"\u0110\u0103ng nh\u1eadp", None))
    # retranslateUi

