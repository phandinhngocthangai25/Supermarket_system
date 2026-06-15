import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# Import tầng Service và giao diện của bạn
from services.Authentication import Authentication
from ui.login import Ui_winLogin
from controllers.LoginController import LoginController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginController()
    window.show()
    sys.exit(app.exec())