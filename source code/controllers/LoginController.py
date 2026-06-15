from ui.login import Ui_winLogin
from PySide6.QtWidgets import QMainWindow, QMessageBox
from services.Authentication import Authentication
from controllers.UserController import UserController

class LoginController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_winLogin()
        self.ui.setupUi(self)

        self.authService = Authentication()

        self.ui.btnLogin.clicked.connect(self.login)

    def login(self):
        
        username = self.ui.txtUsername.text()
        password = self.ui.txtPassword.text()

        is_success = self.authService.login(username, password)
        if is_success:
            QMessageBox.information(self, "Thành công", "Đăng nhập thành công")
            self.close()
            # hiện giao diện người dùng
            self.winUser = UserController()
            self.winUser.show()

        else:
            QMessageBox.warning(self, "Thất bại", "Đăng nhập thất bại")

