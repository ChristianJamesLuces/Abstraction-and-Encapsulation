#Create class named Pet
class Pet:
    #Add a constructor
    def __init__(self, name, animal_type, age):
        #Create data attributes
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    #Create methods
    def set_name(self, name):
        self.name = name
    
    def set_animal_type(self, animal_type):
        self.name = animal_type

    def set_age(self, age):
        self.name = age
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age