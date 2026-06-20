from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QObject, Signal, Qt
from ui.winUser import Ui_winUser
from services.Authentication import Authentication
from controllers.CheckoutController import CheckoutController
from controllers.InvoiceHistoryController import InvoiceHistoryController
from controllers.ProductManagerController import ProductManagerController
from controllers.CustomerManagerController import CustomerManagerController
from controllers.EmployeeManagerController import EmployeeManagerController

class WinUserController(QMainWindow, Ui_winUser):

    logout_request = Signal()

    def __init__(self, user, auth=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.user = user
        self.auth = auth if auth else Authentication(user)

        self._init_pages()
        self._setup_connections()
        self.stackedContent.setCurrentIndex(0)

    def _init_pages(self):

        self.page_checkout = CheckoutController(self.user, self.auth)
        self.stackedContent.addWidget(self.page_checkout)

        self.page_history = InvoiceHistoryController()
        self.stackedContent.addWidget(self.page_history)

        self.page_product = ProductManagerController()
        self.stackedContent.addWidget(self.page_product)

        self.page_customer = CustomerManagerController()
        self.stackedContent.addWidget(self.page_customer)

        self.page_employee = EmployeeManagerController()
        self.stackedContent.addWidget(self.page_employee)

    def _setup_connections(self):

        self.btnPayment.clicked.connect(lambda: self.stackedContent.setCurrentIndex(0))
        self.btnHistory.clicked.connect(lambda: self.stackedContent.setCurrentIndex(1))
        self.btnProduct.clicked.connect(lambda: self.stackedContent.setCurrentIndex(2))
        self.btnCustomer.clicked.connect(lambda: self.stackedContent.setCurrentIndex(3))
        self.btnEmployee.clicked.connect(lambda: self.stackedContent.setCurrentIndex(4))
        self.btnLogout.clicked.connect(self.handle_logout)

    def handle_logout(self):

        self.auth.logout()
        self.logout_request.emit()