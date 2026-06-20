from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QTableWidget
from PySide6.QtCore import Qt
from ui.invoiceDetailDialog import Ui_Dialog
from services.InvoiceService import InvoiceService
from services.CustomerService import CustomerService
from services.EmployeeService import EmployeeService
from services.ProductService import ProductService


class InvoiceDetailDialogController(QDialog, Ui_Dialog):
    def __init__(self, invoice_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.invoice_id = invoice_id
        self.invoice_service = InvoiceService()
        self.customer_service = CustomerService()
        self.employee_service = EmployeeService()
        self.product_service = ProductService()

        self._setup_table()
        self._load_invoice_detail()

    def _setup_table(self):

        self.tableInvoiceDetail.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableInvoiceDetail.setEditTriggers(QTableWidget.NoEditTriggers)

    def _load_invoice_detail(self):

        invoice = self.invoice_service.get_invoice_by_id(self.invoice_id)
        if not invoice:
            self.lblInvoiceID.setText(str(self.invoice_id))
            self.lblDateTime.setText("Không tìm thấy hóa đơn")
            return

        self.lblInvoiceID.setText(str(invoice.invoiceID))
        self.lblDateTime.setText(invoice.date.strftime("%d/%m/%Y %H:%M") if invoice.date else "")

        customer_name = ""
        if invoice.customerID:
            customer = self.customer_service.get_customer_by_id(invoice.customerID)
            if customer:
                customer_name = customer.fullName
        self.lblCustomerName.setText(customer_name)

        employee_name = ""
        if invoice.employeeID:
            employee = self.employee_service.get_employee_by_id(invoice.employeeID)
            if employee:
                employee_name = employee.fullName
        self.lblEmployeeName.setText(employee_name)

        self.lblTotalAmount.setText(f"{invoice.totalAmount:,.0f}")
        self.lblDiscount.setText(f"{invoice.discount:,.0f}")
        self.lblFinalAmount.setText(f"{invoice.finalAmount:,.0f}")

        details = self.invoice_service.get_invoice_detail(self.invoice_id)
        self._display_details(details)

    def _display_details(self, details):
        """Hiển thị chi tiết hóa đơn lên bảng."""
        self.tableInvoiceDetail.setRowCount(len(details))

        for row, detail in enumerate(details):

            product = self.product_service.get_product_by_id(detail.productID)
            product_name = product.name if product else f"ID: {detail.productID}"

            self.tableInvoiceDetail.setItem(row, 0, QTableWidgetItem(product_name))
            self.tableInvoiceDetail.setItem(row, 1, QTableWidgetItem(str(detail.quantity)))
            self.tableInvoiceDetail.setItem(row, 2, QTableWidgetItem(f"{detail.sellingPrice:,.0f}"))
            total = detail.quantity * detail.sellingPrice
            self.tableInvoiceDetail.setItem(row, 3, QTableWidgetItem(f"{total:,.0f}"))