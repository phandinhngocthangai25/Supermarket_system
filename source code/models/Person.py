class Person:

    def __init__(self, fullName="", phone="", email="", address=""):
        self.__fullName = fullName
        self.__phone = phone
        self.__email = email
        self.__address = address

    @property
    def fullName(self):
        return self.__fullName
    
    @fullName.setter
    def fullName(self, fullName):
        self.__fullName = fullName
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address
