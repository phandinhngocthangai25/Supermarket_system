from database.Database import Database 
from models.User import User
from models.Employee import Employee
from models.Customer import Customer
from models.Product import Product
from models.Invoice import Invoice
from models.InvoiceDetail import InvoiceDetail
from services.Authentication import Authentication
import datetime

db = Database()

username1 = "thangpdn"
password1 = "thangdz"

username2 = "tungns"
password2 = "tungvdz"

au = Authentication()
au.login(username1, password1)
print(au.userCurrent.role)

print(datetime.datetime.now())

