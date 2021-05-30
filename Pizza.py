""" 
This class repersents a Pizza   

@authors
Omer Lev-Ron
Sam Medina
"""

from enum import Enum


class Pizza():
    """ Abstract Class """

    def __init__(self, dough=0, sauce=0, cheese=0, toppings=[], is_double_cheese=False, full_topping=True):
        self.__dough = dough
        self.__sauce = sauce
        self.__cheese = cheese
        self.__is_double_cheese = is_double_cheese
        self.__toppings = toppings
        self.__full_topping = full_topping

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if not isinstance(value, Dough):
            raise ValueError("This kind of dough is not allowed.")
        self.__dough = value

    @property
    def sauce(self):
        return self.__sauce
    
    @sauce.setter
    def sauce(self, value):
        if not isinstance(value, Sauce):
            raise ValueError("This kind of sauce is not allowed.")
        self.__sauce = value

    @property
    def cheese(self):
        return self.__cheese
    
    @sauce.setter
    def cheese(self, value):
        if not isinstance(value, Cheese):
            raise ValueError("This kind of cheese is not allowed.")
        self.__cheese = value

    @property
    def toppings(self):
        return self.__toppings
    
    @sauce.setter
    def toppings(self, value):
        if not isinstance(value, Toppings):
            raise ValueError("This kind of topping is not allowed.")
        if len(self.__toppings) < 3:
            self.__toppings.append(value)
        else:
            raise ValueError("The Pizza can have a maximum of 3 toppings")
    
    @property
    def is_double_cheese(self):
        return self.is_double_cheese

    @is_double_cheese.setter
    def is_double_cheese(self, value):
        if not self.cheese:
            raise ValueError("There is no cheese in this pizza")
        self.__is_double_cheese = value
    
    @property
    def full_topping(self):
        return self.__full_topping

    @full_topping.setter
    def full_topping(self, value):
        self.__full_topping = value

    def __str__(self):
        return f"Dough: {self.__dough} \
            \nSauce: {self.__sauce} \
            \nCheese: {self.__cheese} \
            \nIs Double Cheese: {self.__is_double_cheese} \
            \nFull Toppings: {self.__full_topping} \
            \nToppings: {self.__toppings}"

class Dough(Enum):
    THICK = 5
    THIN = 2
    WITHOUT_GLUTEN_THICK = 10
    WITHOUT_GLUTEN_SOFT = 20

    def __str__(self):
        return self.name


class Sauce(Enum):
    TOMATOES = 20
    TOMATOES_AND_CREAM = 40
    SPINACH_AND_CREAM = 23
    PESTO = 120

    def __str__(self):
        return self.name

class Cheese(Enum):
    MOZZARELLA = 280
    PARMESAN = 431
    VEGAN_CHEESE = 50

    def __str__(self):
        return self.name

class Toppings(Enum):
    OLIVES = 115
    CORN = 177
    TOMATOES = 18
    ONION = 40

    def __str__(self):
        return self.name

