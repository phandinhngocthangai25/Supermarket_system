from database.Database import Database
from models.Employee import Employee

class EmployeeService:

    def __init__(self):
        self.db = Database()

    def get_all_employees(self):
        query = "SELECT * FROM Employee ORDER BY employeeID"
        rows = self.db.fetch_all(query)
        return [Employee.from_tuple(row) for row in rows]

    def search_employees(self, keyword):
        if not keyword or not keyword.strip():
            return self.get_all_employees()
        like = f"%{keyword.strip()}%"
        query = """
            SELECT * FROM Employee
            WHERE fullName LIKE ? OR username LIKE ?
            ORDER BY employeeID
        """
        rows = self.db.fetch_all(query, (like, like))
        return [Employee.from_tuple(row) for row in rows]

    def get_employee_by_id(self, employee_id):
        if not employee_id:
            return None
        query = "SELECT * FROM Employee WHERE employeeID = ?"
        row = self.db.fetch_one(query, (employee_id,))
        return Employee.from_tuple(row)

    def get_employee_by_username(self, username):
        query = "SELECT * FROM Employee WHERE username = ?"
        row = self.db.fetch_one(query, (username,))
        return Employee.from_tuple(row)

    def add_employee(self, employee: Employee):
        query = """
            INSERT INTO Employee (fullName, phone, email, address, salary, username, password, role)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            employee.fullName,
            employee.phone,
            employee.email,
            employee.address,
            employee.salary,
            employee.username,
            employee.password,
            employee.role
        )
        self.db.execute_query(query, params)
        return True

    def update_employee(self, employee: Employee):
        query = """
            UPDATE Employee
            SET fullName=?, phone=?, email=?, address=?, salary=?, username=?, password=?, role=?
            WHERE employeeID=?
        """
        params = (
            employee.fullName,
            employee.phone,
            employee.email,
            employee.address,
            employee.salary,
            employee.username,
            employee.password,
            employee.role,
            employee.employeeID
        )
        self.db.execute_query(query, params)
        return True

    def delete_employee(self, employee_id):
        query = "DELETE FROM Employee WHERE employeeID = ?"
        self.db.execute_query(query, (employee_id,))
        return True