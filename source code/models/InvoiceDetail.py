class InvoiceDetail:
    
    def __init__(self, invoiceID=None, productID=None, quantity=0):
        self.__invoiceID = invoiceID
        self.__productID = productID
        self.__quantity = quantity
    
    @property
    def invoiceID(self):
        return self.__invoiceID
    
    @invoiceID.setter
    def invoiceID(self, invoiceID):
        self.__invoiceID = invoiceID

    @property
    def productID(self):
        return self.__productID
    
    @productID.setter
    def productID(self, productID):
        self.__productID = productID

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        if quantity is not None and quantity < 0:
            raise ValueError("Số lượng sản phẩm trong hóa đơn không thể nhỏ hơn 0!")
        self.__quantity = quantity

    @classmethod
    def from_tuple(cls, row):
        if not row:
            return None
        return cls(
            invoiceID=row[0],
            productID=row[1],
            quantity=row[2]
        )