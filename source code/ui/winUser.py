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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_winUser(object):
    def setupUi(self, winUser):
        if not winUser.objectName():
            winUser.setObjectName(u"winUser")
        winUser.resize(1168, 688)
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

        self.frameContent = QFrame(self.centralwidget)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedContent = QStackedWidget(self.frameContent)
        self.stackedContent.setObjectName(u"stackedContent")
        self.pagePayment = QWidget()
        self.pagePayment.setObjectName(u"pagePayment")
        self.horizontalLayout_2 = QHBoxLayout(self.pagePayment)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frameCart = QFrame(self.pagePayment)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 664, 496))
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


        self.horizontalLayout_2.addWidget(self.frameCart)

        self.frameCheckout = QFrame(self.pagePayment)
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


        self.horizontalLayout_2.addWidget(self.frameCheckout)

        self.stackedContent.addWidget(self.pagePayment)
        self.pageHistory = QWidget()
        self.pageHistory.setObjectName(u"pageHistory")
        self.pushButton_2 = QPushButton(self.pageHistory)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(560, 450, 81, 26))
        self.label_4 = QLabel(self.pageHistory)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 130, 49, 16))
        self.stackedContent.addWidget(self.pageHistory)
        self.pageProduct = QWidget()
        self.pageProduct.setObjectName(u"pageProduct")
        self.pushButton = QPushButton(self.pageProduct)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 440, 81, 26))
        self.label_5 = QLabel(self.pageProduct)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 140, 91, 51))
        self.stackedContent.addWidget(self.pageProduct)
        self.pageCustomer = QWidget()
        self.pageCustomer.setObjectName(u"pageCustomer")
        self.pushButton_4 = QPushButton(self.pageCustomer)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(580, 470, 81, 26))
        self.label_2 = QLabel(self.pageCustomer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 110, 91, 61))
        self.stackedContent.addWidget(self.pageCustomer)
        self.pageEmployee = QWidget()
        self.pageEmployee.setObjectName(u"pageEmployee")
        self.pushButton_5 = QPushButton(self.pageEmployee)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(600, 480, 81, 26))
        self.label_3 = QLabel(self.pageEmployee)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 170, 111, 61))
        self.stackedContent.addWidget(self.pageEmployee)

        self.verticalLayout_2.addWidget(self.stackedContent)


        self.horizontalLayout.addWidget(self.frameContent)

        winUser.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(winUser)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1168, 33))
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
        self.btnAddProduct.setText(QCoreApplication.translate("winUser", u"+", None))
        ___qtablewidgetitem = self.tableCartItems.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("winUser", u"STT", None))
        ___qtablewidgetitem1 = self.tableCartItems.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("winUser", u"T\u00ean s\u1ea3n ph\u1ea9m", None))
        ___qtablewidgetitem2 = self.tableCartItems.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("winUser", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        ___qtablewidgetitem3 = self.tableCartItems.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("winUser", u"\u0110\u01a1n gi\u00e1", None))
        ___qtablewidgetitem4 = self.tableCartItems.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("winUser", u"Th\u00e0nh ti\u1ec1n", None))
        self.txtSearchCustomer.setPlaceholderText(QCoreApplication.translate("winUser", u"T\u00ecm kh\u00e1ch h\u00e0ng", None))
        self.txtDiscount.setPlaceholderText(QCoreApplication.translate("winUser", u"S\u1ed1 ti\u1ec1n gi\u1ea3m gi\u00e1", None))
        self.label.setText(QCoreApplication.translate("winUser", u"S\u1ed1 ti\u1ec1n thanh to\u00e1n", None))
        self.txtFinalAmount.setText(QCoreApplication.translate("winUser", u"10000000", None))
        self.pushButton_3.setText(QCoreApplication.translate("winUser", u"Thanh to\u00e1n", None))
        self.pushButton_2.setText(QCoreApplication.translate("winUser", u"2", None))
        self.label_4.setText(QCoreApplication.translate("winUser", u"l\u1ecbch s\u1eed", None))
        self.pushButton.setText(QCoreApplication.translate("winUser", u"1", None))
        self.label_5.setText(QCoreApplication.translate("winUser", u"s\u1ea3n ph\u1ea9m", None))
        self.pushButton_4.setText(QCoreApplication.translate("winUser", u"4", None))
        self.label_2.setText(QCoreApplication.translate("winUser", u"kh\u00e1ch h\u00e0ng", None))
        self.pushButton_5.setText(QCoreApplication.translate("winUser", u"5", None))
        self.label_3.setText(QCoreApplication.translate("winUser", u"nh\u00e2n vi\u00ean", None))
    # retranslateUi

