class Product:

    def __init__(self, productID=None, name="", costPrice=None, sellingPrice=None, quantity=None, unit="", expiryDate=""):
        self.__productID = productID
        self.__name = name
        self.__costPrice = costPrice
        self.__sellingPrice = sellingPrice
        self.__quantity = quantity
        self.__unit = unit
        self.__expiryDate = expiryDate

    @property
    def productID(self):
        return self.__productID
    
    @productID.setter
    def productID(self, productID):
        self.__productID = productID

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def costPrice(self):
        return self.__costPrice
    
    @costPrice.setter
    def costPrice(self, costPrice):
        if costPrice is not None and costPrice < 0:
            raise ValueError("Giá vốn không thể nhỏ hơn 0!")
        self.__costPrice = costPrice
    
    @property
    def sellingPrice(self):
        return self.__sellingPrice
    
    @sellingPrice.setter
    def sellingPrice(self, sellingPrice):
        if sellingPrice is not None and sellingPrice < 0:
            raise ValueError("Giá bán không thể nhỏ hơn 0!")
        self.__sellingPrice = sellingPrice
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        if quantity is not None and quantity < 0:
            raise ValueError("Số lượng tồn kho không thể âm!")
        self.__quantity = quantity
    
    @property
    def unit(self):
        return self.__unit
    
    @unit.setter
    def unit(self, unit):
        self.__unit = unit
    
    @property
    def expiryDate(self):
        return self.__expiryDate
    
    @expiryDate.setter
    def expiryDate(self, expiryDate):
        self.__expiryDate = expiryDate

    @classmethod
    def from_tuple(cls, row):
        if not row:
            return None
        return cls(
            productID=row[0],
            name=row[1],
            costPrice=row[2],
            sellingPrice=row[3],
            quantity=row[4],
            unit=row[5],
            expiryDate=row[6]
        )
    