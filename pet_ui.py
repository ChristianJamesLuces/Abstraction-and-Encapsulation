from pet import Pet

#Create a class
class UserInterface:
    #Add a constructor
    def __init__(self):
        self.pet = Pet(" ", " ", " ")

    #Ask the user inputs
    def pet_name(self):
        name = input("Enter the name of your pet: ")
        self.pet.set_name(name)

    def pet_type(self):
        type = input("Enter the type of your pet (Ex. 'Dog', 'Cat', and 'Bird'): ")
        self.pet.set_animal_type(type)
    
    def pet_age(self):
        age = input("Enter the age of your pet: ")
        self.pet.set_age(age)

    #Display the pet details
    def display_pet_details(self):
        print("Pet's Name: ", self.pet.get_name())
        print("Pet's Type: ", self.pet.get_animal_type())
        print("Pet's Age: ", self.pet.get_age())