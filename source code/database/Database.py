import pyodbc

class Database:

    def __init__(self, conn_str="Driver={ODBC Driver 17 for SQL Server};Server=.;Database=SUPERMARKET_SYSTEM;Trusted_Connection=yes;"):
        self.__conn_str = conn_str

    def get_connection(self):   
        return pyodbc.connect(self.__conn_str)
    
    def execute_query(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            cursor.commit()
        
        except pyodbc.Error as e:
            print(e)
            return False
        finally:
            conn.close()

    def fetch_all(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except pyodbc.Error as e:
            print(e)
            return []
        finally:
            conn.close()
    
    def fetch_one(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchone()
        except pyodbc.Error as e:
            print(e)
            return None
        finally:
            conn.close()
    