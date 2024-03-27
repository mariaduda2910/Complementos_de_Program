from color import Color
from engine import Engine
from person import Person


class Car:
    def __init__(self, owner, color, engine, brand, model, consumption, kms):
        assert isinstance(owner, Person)
        assert isinstance(color, Color)
        assert isinstance(engine, Engine)
        self.owner = owner
        self.color = color
        self.engine = engine
        self.brand = brand
        self.model = model
        self.consumption = consumption
        self.kms = kms

    def __repr__(self):
        return f""" 
                Carro: {self.__model} 
                Dono: {self.__owner}
                Cor: {self.__color}
                Motor: {self.__engine}                    
                """

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def engine(self):
        return self.__engine
    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def consumption(self):
        return self.__consumption
    @consumption.setter
    def consumption(self, consumption):
        self.__consumption = consumption

    @property
    def kms(self):
        return self.__kms
    @kms.setter
    def kms(self, kms):
        self.__kms = kms
