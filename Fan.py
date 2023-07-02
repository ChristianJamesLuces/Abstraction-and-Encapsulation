
#class named Fan to represent a fan
class Fan:
    #Three constants for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    #Add a constructor
    def __init__(self, speed = 1, radius = 5, color = "blue", on = False ):
        self.__speed = speed 
        self.__radius = radius
        self.__color = color
        self.__on = on 

    #Create getter methods
    def get_speed(self):
        return self.__speed
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    
    def get_on(self):
        return self.__on
    
    
