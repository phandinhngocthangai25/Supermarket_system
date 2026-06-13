from database.Database import Database
from models.Invoice import Invoice
from models.InvoiceDetail import InvoiceDetail

class InvoiceService:

    def __init__(self):
        self.db = Database()

    def create_invoice(self, invoice, listInvoiceDetail):
        if not invoice:
            print("The invoice is Node")
            return False
        if not listInvoiceDetail:
            print("The list invoice detail is empty")
            return False
        queryInvoice = """
                    insert into Invoice (customerID, employeeID, totalAmount, discount, finalAmount, paymentMethod, date, note) 
                    output inserted.invoiceID values (?, ?, ?, ?, ?, ?, ?, ?); 
                    commit;
        """
        paramsInvoice = (
            invoice.customerID,
            invoice.employeeID,
            invoice.totalAmount,
            invoice.discount,
            invoice.finalAmount,
            invoice.paymentMethod,
            invoice.date,
            invoice.note
        )
        invoiceID = self.db.fetch_one(queryInvoice,paramsInvoice)
        queryInvoiceDetail = "insert in to InvoiceDetail (invoiceID, productID, quantity, sellingPrice)"
        for invoiceDetail in listInvoiceDetail:
            paramsInvoiceDetail = (
                invoiceID,
                invoiceDetail.productID,
                invoiceDetail.quantity,
                invoiceDetail.sellingPrice
            )
            self.db.execute_query(queryInvoiceDetail, paramsInvoiceDetail)
        print("The invoice has been created successfully")
        return True
    
    @staticmethod
    def calculate_invoice_amount(listInvoiceDetail):
        totalAmount = 0
        for invoiceDetail in listInvoiceDetail:
            totalAmount += invoiceDetail.quantity * invoiceDetail.sellingPrice
        return totalAmount
    
    @staticmethod
    def calculate_invoice_final_amount(listInvoiceDetail, discount=0):
        totalAmount = InvoiceService.calculate_invoice_amount(listInvoiceDetail)
        finalAmount = max(totalAmount - discount, 0)
        return finalAmount
    
    def get_invoice_history(self, start_date, end_date):
        query = "select * from Invoice where date >= ? and date <= ?"
        params = (start_date, end_date)
        invoices_data = self.db.fetch_all(query, params)
        arr_invoice = []
        for invoice in invoices_data:
            arr_invoice.append(Invoice.from_tuple(invoice))
        return arr_invoice
    
    def get_invoice_detail(self, invoiceID):
        query = "select * from InvoiceDetail where invoiceID = ?"
        invoices_detail_data = self.db.fetch_all(query, (invoiceID,))
        arr_invoice_detail = []
        for invoiceDetail in invoices_detail_data:
            arr_invoice_detail.append(InvoiceDetail.from_tuple(invoiceDetail))
        return arr_invoice_detail
    
    @staticmethod
    def calculate_invoice_detail_amount(invoiceDetail):
        totalAmount = invoiceDetail.quantity * invoiceDetail.sellingPrice
        return totalAmount