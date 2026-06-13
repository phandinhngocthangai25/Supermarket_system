from database.Database import Database
from models.Product import Product
class Productservice:

    def __init__(self):
        self.db = Database()

    def get_all_products(self):

        query = "select * from Product"
        products_data = self.db.fetch_all(query)
        arr_products = []
        for product in products_data:
            arr_products.append(Product.from_tuple(product))
        return arr_products
    
    def search_products(self, name):

        if not name or not name.strip():
            return self.get_all_products()
        
        name = name.strip()
        query = "select * from Product where name like ?"
        search_param = f"%{name}%"
        products_data = self.db.fetch_all(query, (search_param,))
        arr_products = []
        for product in products_data:
            arr_products.append(Product.from_tuple(product))
        return arr_products
    
    def add_product(self, product):
        if not product:
            print("The product is none")
            return False
        
        query = "insert into Product (name, costPrice, sellingPrice, quantity, unit, expiryDate) values (?, ?, ?, ?, ?, ?)"
        params = (
            product.name,
            product.costPrice,
            product.sellingPrice,
            product.quantity,
            product.unit,
            product.expiryDate
        )
        self.db.execute_query(query, params)
        print("The product has been added successfully")
        return True
    
    def update_product(self, product):
        if not product:
            print("The product is none")
            return False
        query = """update Product set name = ?, costPrice = ?, sellingPrice = ?, 
                    quantity = ?, unit = ?, expiryDate = ? where productID = ?"""
        params = (
            product.name,
            product.costPrice,
            product.sellingPrice,
            product.quantity,
            product.unit,
            product.expiryDate,
            product.productID
        )
        self.db.execute_query(query, params)
        print("The product has been successfully updated")
        return True
    