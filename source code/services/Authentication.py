from database.Database import Database
from models.User import User
class Authentication:

    def __init__(self, userCurrent=None):
        self.userCurrent = userCurrent
        self.db = Database()
    
    def logout(self):
        self.userCurrent = None

    def login(self, userName, password):
        if not userName.strip() or not password:
            print("The username and password must not be left blank")
            return False
        
        query = "select * from [User] where userName = ? and password = ?"
        user_data = self.db.fetch_one(query, (userName, password))
        if not user_data:
            print("Incorrect username or password")
            return False
        
        self.userCurrent = User.from_tuple(user_data)
        print("ok")
        return True
    
    def change_password(self, oldPassword, newPassword):
            
        if not self.userCurrent:
            print("The current user is empty")
            return False
        
        username = self.userCurrent.userName
        password = self.userCurrent.password
        if password != oldPassword:
            print("Incorret old password")
            return False
        
        query = "update [User] set password = ? where username = ?"
        self.db.execute_query(query, (newPassword, username))
        self.userCurrent.password = newPassword
        print("The password has been successfully changed")
        return True
    
    def is_admin(self):
        if not self.userCurrent:
            print("The current user is empty")
            return False
        return self.userCurrent.role == "Admin" 
        
        