# ProductManagerController.py
from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QMessageBox, QInputDialog, QLineEdit, QDialog, QCompleter
)
from PySide6.QtCore import Qt
from ui.productManager import Ui_product
from services.ProductService import ProductService
from models.Product import Product
from controllers.ProductDialogController import ProductDialogController


class ProductManagerController(QWidget, Ui_product):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.product_service = ProductService()
        self.selected_product_id = None
        self.load_data()
        self._setup_search_completer()
        self._setup_connections()

    def _setup_connections(self):
        self.btnSearch.clicked.connect(self.handle_search)
        self.btnAddProduct.clicked.connect(self.handle_add_product)
        self.btnEditProduct.clicked.connect(self.handle_edit_product)
        # Khi người dùng click chọn 1 dòng -> lưu lại productID đang chọn
        self.tableProduct.itemSelectionChanged.connect(self.handle_row_selected)

    def load_data(self, products=None):

        if products is None:
            products = self.product_service.get_all_products()

        self.tableProduct.setRowCount(0) 

        for row_index, product in enumerate(products):
            self.tableProduct.insertRow(row_index)
            self.tableProduct.setItem(row_index, 0, QTableWidgetItem(str(product.productID)))
            self.tableProduct.setItem(row_index, 1, QTableWidgetItem(product.name))
            self.tableProduct.setItem(row_index, 2, QTableWidgetItem(str(product.quantity)))
            self.tableProduct.setItem(row_index, 3, QTableWidgetItem(str(product.costPrice)))
            self.tableProduct.setItem(row_index, 4, QTableWidgetItem(str(product.sellingPrice)))
            self.tableProduct.setItem(row_index, 5, QTableWidgetItem(product.unit))
            self.tableProduct.setItem(row_index, 6, QTableWidgetItem(str(product.expiryDate)))

    def handle_row_selected(self):

        row = self.tableProduct.currentRow()
        if row < 0:
            self.selected_product_id = None
            return
        id_item = self.tableProduct.item(row, 0)
        self.selected_product_id = id_item.text() if id_item else None

    def handle_search(self):
        keyword = self.txtSearchProduct.text().strip()
        products = self.product_service.search_products(keyword)
        self.load_data(products)

    def handle_add_product(self):

        name, ok = QInputDialog.getText(self, "Thêm sản phẩm", "Tên sản phẩm:")
        if not ok or not name.strip():
            return

        cost_price_str, ok = QInputDialog.getText(self, "Thêm sản phẩm", "Giá nhập:")
        if not ok:
            return

        selling_price_str, ok = QInputDialog.getText(self, "Thêm sản phẩm", "Giá bán:")
        if not ok:
            return

        quantity_str, ok = QInputDialog.getText(self, "Thêm sản phẩm", "Số lượng:")
        if not ok:
            return

        unit, ok = QInputDialog.getText(self, "Thêm sản phẩm", "Đơn vị tính:")
        if not ok:
            return

        expiry_date, ok = QInputDialog.getText(self, "Thêm sản phẩm", "Hạn sử dụng (yyyy-mm-dd):")
        if not ok:
            return

        try:
            cost_price = float(cost_price_str)
            selling_price = float(selling_price_str)
            quantity = int(quantity_str)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Giá và số lượng phải là số hợp lệ!")
            return

        try:
            new_product = Product(
                name=name.strip(),
                costPrice=cost_price,
                sellingPrice=selling_price,
                quantity=quantity,
                unit=unit.strip(),
                expiryDate=expiry_date.strip()
            )
        except ValueError as e:

            QMessageBox.warning(self, "Lỗi dữ liệu", str(e))
            return

        self.product_service.add_product(new_product)
        QMessageBox.information(self, "Thành công", "Đã thêm sản phẩm mới!")
        self.load_data()
        self._setup_search_completer()

    def handle_edit_product(self):
        if not self.selected_product_id:
            QMessageBox.warning(self, "Chưa chọn sản phẩm", "Vui lòng chọn 1 sản phẩm trên bảng để sửa!")
            return

        old_product = self.product_service.get_product_by_id(self.selected_product_id)
        if not old_product:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy sản phẩm!")
            return

        name, ok = QInputDialog.getText(self, "Sửa sản phẩm", "Tên sản phẩm:", QLineEdit.Normal, old_product.name)
        if not ok or not name.strip():
            return

        cost_price_str, ok = QInputDialog.getText(self, "Sửa sản phẩm", "Giá nhập:", QLineEdit.Normal, str(old_product.costPrice))
        if not ok:
            return

        selling_price_str, ok = QInputDialog.getText(self, "Sửa sản phẩm", "Giá bán:", QLineEdit.Normal, str(old_product.sellingPrice))
        if not ok:
            return

        quantity_str, ok = QInputDialog.getText(self, "Sửa sản phẩm", "Số lượng:", QLineEdit.Normal, str(old_product.quantity))
        if not ok:
            return

        unit, ok = QInputDialog.getText(self, "Sửa sản phẩm", "Đơn vị tính:", QLineEdit.Normal, old_product.unit)
        if not ok:
            return

        expiry_date, ok = QInputDialog.getText(self, "Sửa sản phẩm", "Hạn sử dụng:", QLineEdit.Normal, str(old_product.expiryDate))
        if not ok:
            return

        try:
            cost_price = float(cost_price_str)
            selling_price = float(selling_price_str)
            quantity = int(quantity_str)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Giá và số lượng phải là số hợp lệ!")
            return

        try:
            old_product.name = name.strip()
            old_product.costPrice = cost_price
            old_product.sellingPrice = selling_price
            old_product.quantity = quantity
            old_product.unit = unit.strip()
            old_product.expiryDate = expiry_date.strip()
        except ValueError as e:
            QMessageBox.warning(self, "Lỗi dữ liệu", str(e))
            return

        self.product_service.update_product(old_product)
        QMessageBox.information(self, "Thành công", "Đã cập nhật sản phẩm!")
        self.load_data()
        self._setup_search_completer()

    def handle_add_product(self):
        dialog = ProductDialogController(product=None, parent=self)
        if dialog.exec() == QDialog.Accepted:
            new_product = dialog.get_result()
            if new_product:
                success = self.product_service.add_product(new_product)
                if success:
                    QMessageBox.information(self, "Thành công", "Đã thêm sản phẩm mới!")
                    self.load_data()
                    self._setup_search_completer()
                else:
                    QMessageBox.critical(self, "Lỗi", "Thêm sản phẩm thất bại!")

    def handle_edit_product(self):
        if not self.selected_product_id:
            QMessageBox.warning(self, "Chưa chọn", "Vui lòng chọn một sản phẩm để sửa.")
            return

        old_product = self.product_service.get_product_by_id(self.selected_product_id)
        if not old_product:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy sản phẩm.")
            return

        dialog = ProductDialogController(product=old_product, parent=self)
        if dialog.exec() == QDialog.Accepted:
            updated_product = dialog.get_result()
            if updated_product:
                # Giữ nguyên ID
                updated_product.productID = old_product.productID
                success = self.product_service.update_product(updated_product)
                if success:
                    QMessageBox.information(self, "Thành công", "Đã cập nhật sản phẩm!")
                    self.load_data()
                    self._setup_search_completer()
                else:
                    QMessageBox.critical(self, "Lỗi", "Cập nhật sản phẩm thất bại!")

    def _setup_search_completer(self):
        products = self.product_service.get_all_products()
        names = [p.name for p in products]
        completer = QCompleter(names, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.txtSearchProduct.setCompleter(completer)