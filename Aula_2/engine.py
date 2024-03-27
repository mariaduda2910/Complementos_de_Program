
class Engine:
    def __init__(self, fuel, horsepower, torque, displacement, numberCylinders, startingSystem, dryWeight, manufacturer):

        self.fuel = fuel
        self.horsepower = horsepower
        self.torque = torque
        self.displacement = displacement
        self.numberCylinders = numberCylinders
        self.startingSystem = startingSystem
        self.dryWeight = dryWeight
        self.manufacturer = manufacturer

    def __repr__(self):
        return f"""{self.__manufacturer}"""
    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        self.__fuel = fuel

    @property
    def horsepower(self):
        return self.__horsepower

    @horsepower.setter
    def horsepower(self, horsepower):
        self.__horsepower = horsepower

    @property
    def torque(self):
        return self.__torque

    @torque.setter
    def torque(self, torque):
        self.__torque = torque

    @property
    def displacement(self):
        return self.__displacement

    @displacement.setter
    def displacement(self, displacement):
        self.__displacement = displacement

    @property
    def numberCylinders(self):
        return self.__numberCylinders

    @numberCylinders.setter
    def numberCylinders(self, numberCylinders):
        self.__numberCylinders = numberCylinders

    @property
    def startingSystem(self):
        return self.__startingSystem

    @startingSystem.setter
    def startingSystem(self, startingSystem):
        self.__startingSystem = startingSystem

    @property
    def dryWeight(self):
        return self.__dryWeight

    @dryWeight.setter
    def dryWeight(self, dryWeight):
        self.__dryWeight = dryWeight

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer


if __name__ == "__main__":
    # test the class
    v8 = Engine(1,2,3,45,6,7,8,9),
    print(v8)

