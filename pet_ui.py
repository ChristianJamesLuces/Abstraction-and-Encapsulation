from pet import Pet
import PySimpleGUI as sg

#Create a class
class UserInterface:
    #Add a constructor
    def __init__(self):
        self.pet = Pet("", "", "")


    #Ask the user inputs
    def pet_name(self):
        layout = [
            [sg.Text("Enter the name of your pet:")],
            [sg.Input(key="-NAME-")],
            [sg.Button("OK")]
        ]
        window = sg.Window("Pet Name").Layout(layout)
        
        while True:
            event, values = window.Read()
            if event == "OK":
                name = values["-NAME-"]
                self.pet.set_name(name)
                break

        window.Close()

    def pet_type(self):
        layout = [
            [sg.Text("Enter the type of your pet (e.g., 'Dog', 'Cat', 'Bird'):")],
            [sg.Input(key="-TYPE-")],
            [sg.Button("OK")]
        ]
        window = sg.Window("Pet Type").Layout(layout)
        
        while True:
            event, values = window.Read()
            if event == "OK":
                type = values["-TYPE-"]
                self.pet.set_animal_type(type)
                break

        window.Close()

    def pet_age(self):
        layout = [
            [sg.Text("Enter the age of your pet:")],
            [sg.Input(key="-AGE-")],
            [sg.Button("OK")]
        ]
        window = sg.Window("Pet Age").Layout(layout)
        
        while True:
            event, values = window.Read()
            if event == "OK":
                age = values["-AGE-"]
                self.pet.set_age(age)
                break

        window.Close()

    #Display the pet details
    def display_pet_details(self):
        layout = [
            [sg.Text("Pet's Name: "), sg.Text(self.pet.get_name())],
            [sg.Text("Pet's Type: "), sg.Text(self.pet.get_animal_type())],
            [sg.Text("Pet's Age: "), sg.Text(self.pet.get_age())],
            [sg.Button("OK")]
        ]
        window = sg.Window("Pet Details").Layout(layout)
        
        while True:
            event, values = window.Read()
            if event == "OK":
                break

        window.Close()