
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

#A private int data field named speed that specifies the speed of the fan
#A private bool data field named on that specifies whether the fan is on (the default is False)
#A private float data field named radius that specifies the radius of the fan
#A private string data field named color that specifies the color of the fan
#The accessor(getters)  and mutator(setters)  methods for all four data fields
#A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False)

