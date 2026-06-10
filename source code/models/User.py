class User:

    def __init__(self, userID=None, employeeID=None, userName="", password="", role="", createdAt=""):
        self.__userID = userID
        self.__employeeID = employeeID
        self.__userName = userName
        self.__password = password
        self.__role = role
    
    @property
    def userID(self):
        return self.__userID
    
    @userID.setter
    def userID(self, userID):
        self.__userID = userID
    
    @property
    def employeeID(self):
        return self.__employeeID
    
    @employeeID.setter
    def employeeID(self, employeeID):
        self.__employeeID = employeeID
    
    @property
    def userName(self):
        return self.__userName
    
    @userName.setter
    def userName(self, userName):
        self.__userName = userName

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password
    
    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, role):
        self.__role = role

    @property
    def createdAt(self):
        return self.__createdAt
    
    @createdAt.setter
    def createdAt(self, createdAt):
        self.__createdAt = createdAt
    
    @classmethod
    def from_tuple(cls, row):
        if not row:
            return None
        return cls(
            userID=row[0],
            employeeID=row[1],
            userName=row[2],
            password=row[3],
            role=row[4]
        )