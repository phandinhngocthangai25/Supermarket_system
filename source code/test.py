from database.Database import Database
from services.Authentication import Authentication

username = "thangpdn"
password = "thangdz"

au = Authentication()
au.login(username, password)
print(au.userCurrent.role)