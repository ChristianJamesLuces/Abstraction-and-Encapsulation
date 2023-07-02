#Import the modules and files
from pet_ui import UserInterface


#Initialize the class
ui = UserInterface()

#Ask the user's input
ui.pet_name()
ui.pet_type()
ui.pet_age()

#Display the pet's details  
ui.display_pet_details()