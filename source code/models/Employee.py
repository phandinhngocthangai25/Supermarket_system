from models.Person import Person

class Employee(Person):
    def __init__(self, employeeID=None, fullName="", phone="", email="", address="",
                 salary=None, username="", password="", role=""):
        super().__init__(fullName, phone, email, address)
        self.employeeID = employeeID
        self.salary = salary
        self.username = username
        self.password = password
        self.role = role

    @property
    def employeeID(self):
        return self.__employeeID

    @employeeID.setter
    def employeeID(self, value):
        self.__employeeID = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    @classmethod
    def from_tuple(cls, row):
        if not row:
            return None
        return cls(
            employeeID=row[0],
            fullName=row[1],
            phone=row[2],
            email=row[3],
            address=row[4],
            salary=row[5],
            username=row[6],
            password=row[7],
            role=row[8]
        )