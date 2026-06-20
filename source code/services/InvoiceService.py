from database.Database import Database
from models.Invoice import Invoice
from models.InvoiceDetail import InvoiceDetail

class InvoiceService:

    def __init__(self):
        self.db = Database()

    def create_invoice(self, invoice, listInvoiceDetail):
        if not invoice or not listInvoiceDetail:
            return False

        # Tạo hóa đơn
        queryInvoice = """
            INSERT INTO Invoice (customerID, employeeID, totalAmount, discount, finalAmount, paymentMethod, date, note)
            OUTPUT inserted.invoiceID VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            commit;
        """
        paramsInvoice = (invoice.customerID, invoice.employeeID, invoice.totalAmount,
                        invoice.discount, invoice.finalAmount, invoice.paymentMethod,
                        invoice.date, invoice.note)
        row = self.db.fetch_one(queryInvoice, paramsInvoice)
        if not row:
            return False
        invoiceID = row[0]

        # Thêm chi tiết và cập nhật tồn kho
        for detail in listInvoiceDetail:
            # Chèn chi tiết
            queryDetail = "INSERT INTO InvoiceDetail (invoiceID, productID, quantity, sellingPrice) VALUES (?, ?, ?, ?)"
            self.db.execute_query(queryDetail, (invoiceID, detail.productID, detail.quantity, detail.sellingPrice))

            # Giảm số lượng sản phẩm
            updateStock = "UPDATE Product SET quantity = quantity - ? WHERE productID = ?"
            self.db.execute_query(updateStock, (detail.quantity, detail.productID))

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

    def get_invoice_by_id(self, invoice_id):
        """Lấy hóa đơn theo ID, trả về đối tượng Invoice hoặc None"""
        if not invoice_id:
            return None
        query = "SELECT * FROM Invoice WHERE invoiceID = ?"
        row = self.db.fetch_one(query, (invoice_id,))
        if row:
            return Invoice.from_tuple(row)
        return None
    
    @staticmethod
    def calculate_invoice_detail_amount(invoiceDetail):
        totalAmount = invoiceDetail.quantity * invoiceDetail.sellingPrice
        return totalAmount
    
    def get_invoices_with_customer_employee(self, key=None):
        if key and key.strip():
            query = """
                        select Invoice.invoiceID, Customer.fullName, Employee.fullName, finalAmount, [date] from Invoice 
                        left join Customer on Customer.customerID = Invoice.customerID
                        left join Employee on Employee.employeeID = Invoice.employeeID
                        where Employee.fullName like ? or Customer.fullName like ?
                        order by [date] desc
            """
            search_key = f"%{key.strip()}%"
            params = (search_key, search_key)
            rows = self.db.fetch_all(query, params)
            return rows
        else:
            query = """
                        select Invoice.invoiceID, customer.fullName, Employee.fullName, finalAmount, [date] from Invoice 
                        left join Customer on Customer.customerID = Invoice.customerID
                        left join Employee on Employee.employeeID = Invoice.employeeID
                        order by [date] desc
            """
            return self.db.fetch_all(query)
