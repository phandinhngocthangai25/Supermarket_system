from PySide6.QtWidgets import QDialog, QPushButton, QHBoxLayout, QWidget, QMessageBox
from ui.productDialog import Ui_Dialog
from models.Product import Product


class ProductDialogController(QDialog, Ui_Dialog):
    def __init__(self, product: Product = None, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.product = product
        self.setWindowTitle("Sửa sản phẩm" if product else "Thêm sản phẩm")

        self._add_action_buttons()

        if self.product:
            self._fill_data(self.product)

    def _add_action_buttons(self):
        self.btnSave = QPushButton("Lưu")
        self.btnCancel = QPushButton("Hủy")
        btn_container = QWidget(self)
        btn_layout = QHBoxLayout(btn_container)
        btn_layout.addWidget(self.btnSave)
        btn_layout.addWidget(self.btnCancel)

        next_row = self.gridLayout.rowCount()
        self.gridLayout.addWidget(btn_container, next_row, 0, 1, 2)  # 2 cột

        self.btnSave.clicked.connect(self.handle_save)
        self.btnCancel.clicked.connect(self.reject)

    def _fill_data(self, product: Product):
        self.txtName.setText(product.name)
        self.txtQuantity.setText(str(product.quantity))
        self.txtCostPrice.setText(str(product.costPrice))
        self.txtSellingPrice.setText(str(product.sellingPrice))
        self.txtUnit.setText(product.unit)
        self.txTexpiryDate.setText(str(product.expiryDate))

    def get_product(self):

        name = self.txtName.text().strip()
        quantity_str = self.txtQuantity.text().strip()
        cost_str = self.txtCostPrice.text().strip()
        sell_str = self.txtSellingPrice.text().strip()
        unit = self.txtUnit.text().strip()
        expiry = self.txTexpiryDate.text().strip()

        if not name:
            QMessageBox.warning(self, "Thiếu dữ liệu", "Vui lòng nhập tên sản phẩm!")
            return None

        try:
            quantity = int(quantity_str) if quantity_str else 0
            cost_price = float(cost_str) if cost_str else 0
            selling_price = float(sell_str) if sell_str else 0
        except ValueError:
            QMessageBox.warning(self, "Lỗi dữ liệu", "Số lượng và giá phải là số hợp lệ!")
            return None

        return Product(
            name=name,
            quantity=quantity,
            costPrice=cost_price,
            sellingPrice=selling_price,
            unit=unit,
            expiryDate=expiry
        )

    def handle_save(self):

        product = self.get_product()
        if product is not None:
            self._product = product
            self.accept()

    def get_result(self):
        return getattr(self, '_product', None)