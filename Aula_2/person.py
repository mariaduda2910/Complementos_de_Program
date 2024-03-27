class Person():
    def __init__(self, forename, surname, address, CC, phone):
        self.forename = forename
        self.surname = surname
        self.address = address
        self.CC = CC
        self.phone = phone

    def __repr__(self):
        return f"{self.__forename} {self.__surname} -- CC: {self.__CC}"

    @property
    def forename(self):
        return self.__forename.title()

    @forename.setter
    def forename(self, forename):
        assert isinstance(forename, str), " "
        self.__forename = forename.title()

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def CC(self):
        return self.__CC

    @CC.setter
    def CC(self, CC):
        self.__CC = CC

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone
