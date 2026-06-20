import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QObject, Signal
from ui.login import Ui_winLogin
from services.Authentication import Authentication
from controllers.WinUserController import WinUserController



class LoginController(QMainWindow, Ui_winLogin):

    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.auth = Authentication()
        self.btnLogin.clicked.connect(self.handle_login)
        self.txtUsername.returnPressed.connect(self.handle_login)
        self.txtPassword.returnPressed.connect(self.handle_login)

    def handle_login(self):

        username = self.txtUsername.text().strip()
        password = self.txtPassword.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu.")
            return

        if self.auth.login(username, password):

            QMessageBox.information(self, "Thông báo", "Đăng nhập thành công!")
            self.txtUsername.clear()
            self.txtPassword.clear()
            self.open_main_window()
        else:

            QMessageBox.critical(self, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu.")

    def open_main_window(self):

        user = self.auth.userCurrent
        self.main_window = WinUserController(user, self.auth)
        self.main_window.logout_request.connect(self.process_logout)
        self.main_window.show()
        self.hide()

    def process_logout(self):

        if self.main_window:
            self.main_window.close()
            self.main_window = None
            self.show()