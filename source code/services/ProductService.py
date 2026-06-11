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

        if not name.strip():
            return self.get_all_products()

        query = "select * from Product where name like ?"
        search_param = f"%{name}%"
        products_data = self.db.fetch_all(query, (search_param,))
        arr_products = []
        for product in products_data:
            arr_products.append(Product.from_tuple(product))
        return arr_products
