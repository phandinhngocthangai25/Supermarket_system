from database.Database import Database

class ReportService:

    def __init__(self):
        self.db = Database()

    def get_revenue_by_date_range(self, from_date, to_date):
        query = """SELECT SUM(finalAmount) FROM Invoice 
                   WHERE date BETWEEN ? AND ?"""
        result = self.db.fetch_one(query, (from_date, to_date))
        return result[0] if result and result[0] is not None else 0

    def get_top_selling_products(self, limit=5):
        query = """
            SELECT p.productID, p.name, SUM(id.quantity) as TotalSold
            FROM InvoiceDetail id
            JOIN Product p ON id.productID = p.productID
            GROUP BY p.productID, p.name
            ORDER BY TotalSold DESC
        """
        result = self.db.fetch_all(query)
        return result[:limit]

    def get_low_stock_alerts(self, threshold=10):
        query = "SELECT productID, name, quantity, unit FROM Product WHERE quantity <= ?"
        return self.db.fetch_all(query, (threshold,))

    def get_expired_products_alerts(self, current_date):
        query = "SELECT productID, name, quantity, expiryDate FROM Product WHERE expiryDate <= ?"
        return self.db.fetch_all(query, (current_date,))