from database.Database import Database
from models.User import User

class Authentication:
    def __init__(self, userCurrent=None):
        self.userCurrent = userCurrent
        self.db = Database()

    def login(self, userName, password):
        if not userName.strip() or not password:
            print("Username and password cannot be empty")
            return False

        # Truy vấn trên bảng Employee
        query = "SELECT * FROM Employee WHERE username = ? AND password = ?"
        row = self.db.fetch_one(query, (userName, password))
        if not row:
            print("Incorrect username or password")
            return False

        self.userCurrent = User(
            userID=row[0],
            employeeID=row[0],
            userName=row[6],
            password=row[7],
            role=row[8]
        )
        print("Login successful")
        return True

    def logout(self):
        self.userCurrent = None

    def change_password(self, oldPassword, newPassword):
        if not self.userCurrent:
            print("No user logged in")
            return False
        # Kiểm tra mật khẩu cũ
        if self.userCurrent.password != oldPassword:
            print("Old password incorrect")
            return False
        # Cập nhật trên bảng Employee
        query = "UPDATE Employee SET password = ? WHERE employeeID = ?"
        self.db.execute_query(query, (newPassword, self.userCurrent.employeeID))
        self.userCurrent.password = newPassword
        print("Password changed successfully")
        return True

    def is_admin(self):
        return self.userCurrent and self.userCurrent.role == "Admin"