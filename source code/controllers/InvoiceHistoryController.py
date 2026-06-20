from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QTableWidget, QCompleter
from PySide6.QtCore import Qt
from ui.invoiceHistory import Ui_invoice
from services.InvoiceService import InvoiceService
from controllers.InvoiceDetailDialogController import InvoiceDetailDialogController


class InvoiceHistoryController(QWidget, Ui_invoice):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.invoice_service = InvoiceService()

        self.tableInvoice.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableInvoice.setEditTriggers(QTableWidget.NoEditTriggers)

        self.load_invoices()
        self.setup_completer()

        self.btnSearch.clicked.connect(self.search_invoices)
        self.txtSearch.returnPressed.connect(self.search_invoices)
        self.tableInvoice.cellDoubleClicked.connect(self.open_invoice_detail)

    def setup_completer(self):

        rows = self.invoice_service.get_invoices_with_customer_employee()
        suggestions = []
        for row in rows:
            invoice_id = str(row[0]) if row[0] else ""
            customer_name = row[1] if row[1] else ""
            employee_name = row[2] if row[2] else ""
            if customer_name:
                suggestions.append(customer_name)
            if employee_name:
                suggestions.append(employee_name)
            if invoice_id:
                suggestions.append(invoice_id)

        suggestions = list(set([s.strip() for s in suggestions if s.strip()]))
        completer = QCompleter(suggestions, self.txtSearch)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.txtSearch.setCompleter(completer)

    def load_invoices(self):

        rows = self.invoice_service.get_invoices_with_customer_employee()
        self._display_invoices(rows)

    def search_invoices(self):

        keyword = self.txtSearch.text().strip()
        rows = self.invoice_service.get_invoices_with_customer_employee(keyword)
        self._display_invoices(rows)

    def _display_invoices(self, rows):

        self.tableInvoice.setRowCount(len(rows))
        for row_idx, data in enumerate(rows):
            invoice_id, customer_name, employee_name, final_amount, date = data
            self.tableInvoice.setItem(row_idx, 0, QTableWidgetItem(str(invoice_id)))
            self.tableInvoice.setItem(row_idx, 1, QTableWidgetItem(customer_name or ""))
            self.tableInvoice.setItem(row_idx, 2, QTableWidgetItem(employee_name or ""))
            amount_text = f"{final_amount:,.0f}" if final_amount is not None else "0"
            self.tableInvoice.setItem(row_idx, 3, QTableWidgetItem(amount_text))
            self.tableInvoice.setItem(row_idx, 4, QTableWidgetItem(str(date) if date else ""))
    
    def open_invoice_detail(self, row, column):

        invoice_id_item = self.tableInvoice.item(row, 0)
        if invoice_id_item is None:
            return
        try:
            invoice_id = int(invoice_id_item.text())
        except ValueError:
            return

        dialog = InvoiceDetailDialogController(invoice_id, self)
        dialog.exec()