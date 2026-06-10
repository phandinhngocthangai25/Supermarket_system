from database.Database import Database 
from models.User import User
from models.Employee import Employee
from models.Customer import Customer
from models.Product import Product
from models.Invoice import Invoice
from models.InvoiceDetail import InvoiceDetail

db = Database()

a = (1, 1, "thang123", "nhân viên", "123123")
u1 = User.from_tuple(a)
print(u1.role)
