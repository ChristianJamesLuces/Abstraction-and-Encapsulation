#Create a class named Car
class Car:
    #Add a Constructor
    def __init__(self, year_model, make, speed = 0 ):
        #Create the data attributes
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

#Create methods