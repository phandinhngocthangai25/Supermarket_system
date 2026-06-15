from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui.winUser import Ui_winUser

class UserController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_winUser()
        self.ui.setupUi(self)

    