from pet import Pet

#Create a class
class Pet:
    #Add a constructor
    def __init__(self):
        self.pet = Pet()

    #Ask the user inputs
    def pet_name(self):
        name = input("Enter the name of your pet: ")
        self.pet.set_name(name)

    def pet_type(self):
        type = input("Enter the type of your pet: ")
        self.pet.set_type(type)
    
    def pet_age(self):
        age = input("Enter the age of your pet: ")
        self.pet.set_age(type)

    #Display the pet details
    
