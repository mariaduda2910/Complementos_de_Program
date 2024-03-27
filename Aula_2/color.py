class Color:
    def __init__(self, colorName, r, g, b):
        self.colorName = colorName
        self.r, self.g, self.b = r, g, b

    def __repr__(self):
        return f"""{self.__colorName}"""
    @property
    def colorName(self):
        return self.__colorName

    @colorName.setter
    def colorName(self, colorName):
        self.__colorName = colorName

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        self.__r = r

    @property
    def g(self):
        return self.__g

    @g.setter
    def g(self, g):
        self.__g = g

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b


if __name__ == "__main__":
    # test the class
    red = Color("red", 1, 2, 3)
    print(red)