from models.Person import Person
class Customer(Person):

    def __init__(self, customerID=None, fullName="", phone="", email="", address="", loyaltyPoints=0, createdAt=""):
        super().__init__(fullName, phone, email, address)
        self.customerID = customerID
        self.loyaltyPoints = loyaltyPoints

    @property
    def customerID(self):
        return self.__customerID
    
    @customerID.setter
    def customerID(self, customerID):
        self.__customerID = customerID

    @property
    def loyaltyPoints(self):
        return self.__loyaltyPoints
    
    @loyaltyPoints.setter
    def loyaltyPoints(self, loyaltyPoints):
        self.__loyaltyPoints = loyaltyPoints

    @classmethod
    def from_tuple(cls, row):
        if not row:
            return None
        return cls(
            customerID=row[0],
            fullName=row[1],
            phone=row[2],
            email=row[3],
            address=row[4],
            loyaltyPoints=row[5]
        )
    