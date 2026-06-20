import datetime
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QPushButton,
    QHeaderView, QSpinBox, QCompleter, QTableWidget
)
from PySide6.QtCore import Qt, QStringListModel
from ui.checkout import Ui_chechout
from services.ProductService import ProductService
from services.CustomerService import CustomerService
from services.InvoiceService import InvoiceService
from models.Invoice import Invoice
from models.InvoiceDetail import InvoiceDetail


class CheckoutController(QWidget, Ui_chechout):
    def __init__(self, user, auth, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.user = user
        self.auth = auth
        self.product_service = ProductService()
        self.customer_service = CustomerService()
        self.invoice_service = InvoiceService()

        self.cart_items = []
        self.selected_customer_id = None

        self._setup_ui()
        self._connect_signals()
        self.setup_completers()
        self.update_cart_table()

    def _setup_ui(self):
        self.tableCartItems.setEditTriggers(QTableWidget.NoEditTriggers)  # không chỉnh sửa trực tiếp
        self.tableCartItems.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableCartItems.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)

    def _connect_signals(self):
        self.btnAddProduct.clicked.connect(self.add_product_from_search)
        self.txtSearchProduct.returnPressed.connect(self.add_product_from_search)
        self.txtDiscount.textChanged.connect(self.update_final_amount)
        self.txtSearchCustomer.returnPressed.connect(self.search_customer)
        self.pushButton_3.clicked.connect(self.handle_payment)

    def setup_completers(self):
        products = self.product_service.get_all_products()
        product_names = [p.name for p in products if p.name.strip()]
        completer_product = QCompleter(product_names, self.txtSearchProduct)
        completer_product.setCaseSensitivity(Qt.CaseInsensitive)
        completer_product.setFilterMode(Qt.MatchContains)
        self.txtSearchProduct.setCompleter(completer_product)

        customers = self.customer_service.get_all_customers()
        customer_names = [c.fullName for c in customers if c.fullName.strip()]
        completer_customer = QCompleter(customer_names, self.txtSearchCustomer)
        completer_customer.setCaseSensitivity(Qt.CaseInsensitive)
        completer_customer.setFilterMode(Qt.MatchContains)
        self.txtSearchCustomer.setCompleter(completer_customer)

    def add_product_from_search(self):
        keyword = self.txtSearchProduct.text().strip()
        if not keyword:
            return

        products = self.product_service.search_products(keyword)
        if not products:
            QMessageBox.warning(self, "Không tìm thấy", "Không tìm thấy sản phẩm nào.")
            return

        product = products[0]
        self.add_product_to_cart(product)
        self.txtSearchProduct.clear()

    def add_product_to_cart(self, product):
        for item in self.cart_items:
            if item['product'].productID == product.productID:
                if item['quantity'] + 1 > product.quantity:
                    QMessageBox.warning(self, "Lỗi", f"Số lượng vượt quá tồn kho ({product.quantity})")
                    return
                item['quantity'] += 1
                self.update_cart_table()
                return

        if product.quantity < 1:
            QMessageBox.warning(self, "Lỗi", "Sản phẩm đã hết hàng.")
            return
        self.cart_items.append({
            'product': product,
            'quantity': 1,
            'sellingPrice': product.sellingPrice
        })
        self.update_cart_table()

    def update_cart_table(self):
        self.tableCartItems.blockSignals(True)
        self.tableCartItems.setRowCount(len(self.cart_items))

        for row, item in enumerate(self.cart_items):
            product = item['product']

            self.tableCartItems.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.tableCartItems.setItem(row, 1, QTableWidgetItem(product.name))

            spin = QSpinBox()
            spin.setMinimum(1)
            spin.setMaximum(product.quantity)
            spin.setValue(item['quantity'])
            spin.valueChanged.connect(lambda value, r=row: self.on_quantity_changed(r, value))
            self.tableCartItems.setCellWidget(row, 2, spin)

            self.tableCartItems.setItem(row, 3, QTableWidgetItem(f"{item['sellingPrice']:,.0f}"))
            total = item['quantity'] * item['sellingPrice']
            self.tableCartItems.setItem(row, 4, QTableWidgetItem(f"{total:,.0f}"))
            btn_del = QPushButton("Xóa")
            btn_del.clicked.connect(lambda _, r=row: self.remove_cart_item(r))
            self.tableCartItems.setCellWidget(row, 5, btn_del)

        self.tableCartItems.blockSignals(False)
        self.update_final_amount()

    def on_quantity_changed(self, row, new_value):
        item = self.cart_items[row]
        product = item['product']
        if new_value > product.quantity:
            QMessageBox.warning(self, "Lỗi", f"Số lượng vượt quá tồn kho ({product.quantity})")
            spin = self.tableCartItems.cellWidget(row, 2)
            if spin:
                spin.setValue(item['quantity'])
            return
        item['quantity'] = new_value
        total = new_value * item['sellingPrice']
        self.tableCartItems.setItem(row, 4, QTableWidgetItem(f"{total:,.0f}"))
        self.update_final_amount()

    def remove_cart_item(self, row):
        if 0 <= row < len(self.cart_items):
            del self.cart_items[row]
            self.update_cart_table()

    def calculate_total(self):
        return sum(item['quantity'] * item['sellingPrice'] for item in self.cart_items)

    def update_final_amount(self):
        total = self.calculate_total()
        discount_text = self.txtDiscount.text().strip()
        discount = float(discount_text) if discount_text else 0
        final = max(total - discount, 0)
        self.txtFinalAmount.setText(f"{final:,.0f}")

    def search_customer(self):
        keyword = self.txtSearchCustomer.text().strip()
        if not keyword:
            self.selected_customer_id = None
            return

        customers = self.customer_service.search_customers(keyword)
        if not customers:
            QMessageBox.warning(self, "Không tìm thấy", "Không tìm thấy khách hàng nào.")
            self.selected_customer_id = None
            return

        customer = customers[0]
        self.selected_customer_id = customer.customerID
        self.txtSearchCustomer.setText(customer.fullName)
        QMessageBox.information(self, "Đã chọn", f"Đã chọn khách hàng: {customer.fullName}")

    def handle_payment(self):
        if not self.cart_items:
            QMessageBox.warning(self, "Giỏ hàng trống", "Chưa có sản phẩm trong giỏ.")
            return

        employee_id = self.user.employeeID if self.user else None
        if not employee_id:
            QMessageBox.warning(self, "Lỗi", "Không xác định được nhân viên.")
            return

        total = self.calculate_total()
        discount_text = self.txtDiscount.text().strip()
        discount = float(discount_text) if discount_text else 0
        final = max(total - discount, 0)
        print(self.selected_customer_id)
        invoice = Invoice(
            customerID=self.selected_customer_id,
            employeeID=employee_id,
            totalAmount=total,
            discount=discount,
            finalAmount=final,
            paymentMethod="Tiền mặt",
            date=datetime.datetime.now(),
            note=""
        )

        details = [
            InvoiceDetail(
                productID=item['product'].productID,
                quantity=item['quantity'],
                sellingPrice=item['sellingPrice']
            )
            for item in self.cart_items
        ]

        success = self.invoice_service.create_invoice(invoice, details)
        if success:
            QMessageBox.information(self, "Thành công", "Hóa đơn đã được tạo.")
            # Xóa giỏ
            self.cart_items.clear()
            self.update_cart_table()
            self.txtDiscount.clear()
            self.selected_customer_id = None
            self.txtSearchCustomer.clear()

            self.setup_completers()
        else:
            QMessageBox.critical(self, "Lỗi", "Không thể tạo hóa đơn.")