from database.Database import Database
from models.Customer import Customer

class CustomerService:

    def __init__(self):
        self.db = Database()

    def get_all_customers(self):

        query = "SELECT * FROM Customer"
        customers_data = self.db.fetch_all(query)
        
        arr_customers = []
        for row in customers_data:
            arr_customers.append(Customer.from_tuple(row))
        return arr_customers

    def get_customer_by_id(self, customer_id):
        """Lấy thông tin khách hàng theo ID, trả về đối tượng Customer hoặc None"""
        if not customer_id:
            return None
        query = "SELECT * FROM Customer WHERE customerID = ?"
        row = self.db.fetch_one(query, (customer_id,))
        if row:
            return Customer.from_tuple(row)
        return None

    def search_customers(self, keyword):

        if not keyword or not keyword.strip():
            return self.get_all_customers()
        
        keyword = keyword.strip()
        query = "SELECT * FROM Customer WHERE fullName LIKE ? OR phone LIKE ?"
        search_param = f"%{keyword}%"
        customers_data = self.db.fetch_all(query, (search_param, search_param))
        
        arr_customers = []
        for row in customers_data:
            arr_customers.append(Customer.from_tuple(row))
        return arr_customers
    
    def add_customer(self, customer):
        if not customer:
            print("Customer object is none")
            return False
            
        query = "INSERT INTO Customer (fullName, phone, email, address, loyaltyPoints) VALUES (?, ?, ?, ?, ?)"
        params = (
            customer.fullName, 
            customer.phone, 
            customer.email,
            customer.address,
            customer.loyaltyPoints
        )
        self.db.execute_query(query, params)
        print("Customer has been added successfully")
        return True
    
    def update_customer(self, customer):
        """Cập nhật thông tin từ một đối tượng Customer"""
        if not customer:
            print("Customer object is none")
            return False

        query = """UPDATE Customer SET fullName = ?, phone = ?, email = ?, address = ?, loyaltyPoints = ? WHERE customerID = ?"""
        params = (
            customer.fullName, 
            customer.phone, 
            customer.email,
            customer.address,  
            customer.loyaltyPoints, 
            customer.customerID
        )
        self.db.execute_query(query, params)
        print("Customer has been updated successfully")
        return True

    def update_points(self, customer_id, added_points):
        query = "UPDATE Customer SET loyaltyPoints = loyaltyPoints + ? WHERE customerID = ?"
        self.db.execute_query(query, (added_points, customer_id))
        return True