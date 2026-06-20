from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QTableWidget, QCompleter
from PySide6.QtCore import Qt
from ui.customerManager import Ui_customer
from services.CustomerService import CustomerService
from models.Customer import Customer


class CustomerManagerController(QWidget, Ui_customer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.customer_service = CustomerService()
        self.current_customer_id = None 

        self.tableCustomer.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableCustomer.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableCustomer.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableCustomer.setSelectionMode(QTableWidget.SingleSelection)

        self.load_customers()
        self.setup_completer()

        self.btnSearchCustomer.clicked.connect(self.search_customers)
        self.txtSearchCustomer.returnPressed.connect(self.search_customers)
        self.btnAddCustomer.clicked.connect(self.add_customer)
        self.btnEditCustomer.clicked.connect(self.edit_customer)
        self.tableCustomer.itemSelectionChanged.connect(self.on_selection_changed)

        self.btnEditCustomer.setEnabled(False)

    def load_customers(self):
        customers = self.customer_service.get_all_customers()
        self._display_customers(customers)

    def search_customers(self):
        keyword = self.txtSearchCustomer.text().strip()
        if keyword:
            customers = self.customer_service.search_customers(keyword)
        else:
            customers = self.customer_service.get_all_customers()
        self._display_customers(customers)

    def _display_customers(self, customers):
        self.tableCustomer.setRowCount(len(customers))
        for row, customer in enumerate(customers):
            self.tableCustomer.setItem(row, 0, QTableWidgetItem(str(customer.customerID)))
            self.tableCustomer.setItem(row, 1, QTableWidgetItem(customer.fullName))
            self.tableCustomer.setItem(row, 2, QTableWidgetItem(customer.phone))
            self.tableCustomer.setItem(row, 3, QTableWidgetItem(customer.email))
            self.tableCustomer.setItem(row, 4, QTableWidgetItem(customer.address))
            self.tableCustomer.setItem(row, 5, QTableWidgetItem(str(customer.loyaltyPoints)))
        self.current_customer_id = None
        self.btnEditCustomer.setEnabled(False)

    def on_selection_changed(self):
        selected = self.tableCustomer.selectedItems()
        if selected:
            row = selected[0].row()
            id_item = self.tableCustomer.item(row, 0)
            if id_item:
                self.current_customer_id = int(id_item.text())
                self.btnEditCustomer.setEnabled(True)
        else:
            self.current_customer_id = None
            self.btnEditCustomer.setEnabled(False)

    def add_customer(self):
        dialog = CustomerEditDialog(self)
        if dialog.exec() == QDialog.Accepted:
            customer = dialog.get_customer()
            if customer:
                success = self.customer_service.add_customer(customer)
                if success:
                    QMessageBox.information(self, "Thành công", "Thêm khách hàng thành công.")
                    self.load_customers()
                    self.setup_completer()
                else:
                    QMessageBox.critical(self, "Lỗi", "Thêm khách hàng thất bại.")

    def edit_customer(self):
        if self.current_customer_id is None:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn khách hàng cần sửa.")
            return

        customer = self.customer_service.get_customer_by_id(self.current_customer_id)
        if not customer:
            QMessageBox.critical(self, "Lỗi", "Không tìm thấy khách hàng.")
            return

        dialog = CustomerEditDialog(self, customer)
        if dialog.exec() == QDialog.Accepted:
            updated_customer = dialog.get_customer()
            if updated_customer:
                updated_customer.customerID = self.current_customer_id
                success = self.customer_service.update_customer(updated_customer)
                if success:
                    QMessageBox.information(self, "Thành công", "Cập nhật khách hàng thành công.")
                    self.load_customers()
                    self.setup_completer()
                else:
                    QMessageBox.critical(self, "Lỗi", "Cập nhật khách hàng thất bại.")

    def setup_completer(self):
        """Tạo danh sách gợi ý tên khách hàng cho ô tìm kiếm."""
        customers = self.customer_service.get_all_customers()
        names = [c.fullName for c in customers if c.fullName.strip()]
        completer = QCompleter(names, self.txtSearchCustomer)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.txtSearchCustomer.setCompleter(completer)

class CustomerEditDialog(QDialog):
    def __init__(self, parent=None, customer=None):
        super().__init__(parent)
        self.setWindowTitle("Thông tin khách hàng")
        self.setModal(True)
        self.setMinimumWidth(400)

        self.customer = customer
        layout = QVBoxLayout(self)

        form = QFormLayout()
        self.txtFullName = QLineEdit()
        self.txtPhone = QLineEdit()
        self.txtEmail = QLineEdit()
        self.txtAddress = QLineEdit()
        self.txtLoyaltyPoints = QLineEdit()

        form.addRow("Họ và tên:", self.txtFullName)
        form.addRow("Số điện thoại:", self.txtPhone)
        form.addRow("Email:", self.txtEmail)
        form.addRow("Địa chỉ:", self.txtAddress)
        form.addRow("Điểm thưởng:", self.txtLoyaltyPoints)

        layout.addLayout(form)

        btn_layout = QHBoxLayout()
        btn_save = QPushButton("Lưu")
        btn_cancel = QPushButton("Hủy")
        btn_save.clicked.connect(self.accept)
        btn_cancel.clicked.connect(self.reject)
        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_cancel)
        layout.addLayout(btn_layout)

        if customer:
            self.txtFullName.setText(customer.fullName)
            self.txtPhone.setText(customer.phone)
            self.txtEmail.setText(customer.email)
            self.txtAddress.setText(customer.address)
            self.txtLoyaltyPoints.setText(str(customer.loyaltyPoints))

    def get_customer(self):
        """Tạo đối tượng Customer từ dữ liệu nhập."""
        full_name = self.txtFullName.text().strip()
        if not full_name:
            QMessageBox.warning(self, "Cảnh báo", "Họ tên không được để trống.")
            return None

        phone = self.txtPhone.text().strip()
        email = self.txtEmail.text().strip()
        address = self.txtAddress.text().strip()
        try:
            loyalty_points = int(self.txtLoyaltyPoints.text().strip()) if self.txtLoyaltyPoints.text().strip() else 0
            if loyalty_points < 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Cảnh báo", "Điểm thưởng phải là số nguyên không âm.")
            return None

        return Customer(
            fullName=full_name,
            phone=phone,
            email=email,
            address=address,
            loyaltyPoints=loyalty_points
        )
    
    