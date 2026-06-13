import datetime

class Invoice:
    def __init__(self, invoiceID=None, customerID=None, 
                 employeeID=None, totalAmount=0, discount=0,
                 finalAmount=0, paymentMethod="", date=None, note=""):
        self.invoiceID = invoiceID
        self.customerID = customerID
        self.employeeID = employeeID
        self.totalAmount = totalAmount
        self.discount = discount
        self.finalAmount = finalAmount
        self.paymentMethod = paymentMethod
        self.date = date if date else datetime.datetime.now()
        self.note = note

    @property
    def invoiceID(self):
        return self.__invoiceID
    
    @invoiceID.setter
    def invoiceID(self, invoiceID):
        self.__invoiceID = invoiceID
    
    @property
    def customerID(self):
        return self.__customerID
    
    @customerID.setter
    def customerID(self, customerID):
        self.__customerID = customerID

    @property
    def employeeID(self):
        return self.__employeeID
    
    @employeeID.setter
    def employeeID(self, employeeID):
        self.__employeeID = employeeID

    @property
    def totalAmount(self):
        return self.__totalAmount
    
    @totalAmount.setter
    def totalAmount(self, totalAmount):
        if totalAmount is not None and totalAmount < 0:
            raise ValueError("Tổng tiền không thể nhỏ hơn 0!")
        self.__totalAmount = totalAmount

    @property
    def discount(self):
        return self.__discount
    
    @discount.setter
    def discount(self, discount):
        if discount is not None and discount < 0:
            raise ValueError("Mức giảm giá không thể nhỏ hơn 0!")
        self.__discount = discount

    @property
    def finalAmount(self):
        return self.__finalAmount
    
    @finalAmount.setter
    def finalAmount(self, finalAmount):
        if finalAmount is not None and finalAmount < 0:
            raise ValueError("Số tiền cuối cùng không thể nhỏ hơn 0!")
        self.__finalAmount = finalAmount

    @property
    def paymentMethod(self):
        return self.__paymentMethod
    
    @paymentMethod.setter
    def paymentMethod(self, paymentMethod):
        self.__paymentMethod = paymentMethod

    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def note(self):
        return self.__note
    
    @note.setter
    def note(self, note):
        self.__note = note

    @classmethod
    def from_tuple(cls, row):
        if not row:
            return None
        return cls(
            invoideID=row[0],
            customerID=row[1],
            employeeID=row[2],
            totalAmount=row[3],
            discount=row[4],
            finalAmount=row[5],
            paymentMethod=row[6],
            date=row[7],
            note=row[8]
        )