#Create a class named Car
class Car:
    #Add a Constructor
    def __init__(self, year_model, make, speed = 0 ):
        #Create data attributes
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    #Create methods
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed
    
    