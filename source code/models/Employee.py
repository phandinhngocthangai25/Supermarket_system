from models.Person import Person
class Employee(Person):

    def __init__(self, employeeID=None, fullName="", phone="", email="", address="", salary=None):
        super().__init__(fullName, phone, email, address)
        self.__employeeID = employeeID
        self.__salary = salary

    @property
    def employeeID(self):
        return self.__employeeID
    
    @employeeID.setter
    def employeeID(self, employeeID):
        self.__employeeID = employeeID

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @classmethod
    def from_tuple(cls, row):
        if not row:
            return None
        return cls(
            employeeID=row[0],
            fullName=row[1], 
            phone=row[3], 
            email=row[4], 
            address=row[5], 
            salary=row[6]
        )