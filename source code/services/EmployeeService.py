from database.Database import Database

class EmployeeService:

    def __init__(self):
        self.db = Database()

    def check_login(self, username, password):
        query = "SELECT * FROM Employee WHERE username = ? AND password = ?"
        result = self.db.fetch_one(query, (username.strip(), password.strip()))
        return result

    def get_all_employees(self):
        """Lấy toàn bộ danh sách nhân viên"""
        query = "SELECT * FROM Employee"
        return self.db.fetch_all(query)
    
    def search_employees(self, name):
        """Tìm kiếm nhân viên theo tên"""
        if not name or not name.strip():
            return self.get_all_employees()
            
        name = name.strip()
        query = "SELECT * FROM Employee WHERE name LIKE ?"
        return self.db.fetch_all(query, (f"%{name}%",))
    
    def add_employee(self, name, role, username, password, phone_number=""):
        """Thêm nhân viên mới vào hệ thống"""
        query = """INSERT INTO Employee (name, role, username, password, phoneNumber) 
                   VALUES (?, ?, ?, ?, ?)"""
        params = (name.strip(), role.strip(), username.strip(), password.strip(), phone_number.strip())
        self.db.execute_query(query, params)
        print("Employee has been added successfully")
        return True
    
    def update_employee(self, employee_id, name, role, username, password, phone_number):
        """Cập nhật thông tin hoặc đổi mật khẩu/quyền hạn nhân viên"""
        query = """UPDATE Employee 
                   SET name = ?, role = ?, username = ?, password = ?, phoneNumber = ? 
                   WHERE employeeID = ?"""
        params = (name.strip(), role.strip(), username.strip(), password.strip(), phone_number.strip(), employee_id)
        self.db.execute_query(query, params)
        print("Employee has been updated successfully")
        return True