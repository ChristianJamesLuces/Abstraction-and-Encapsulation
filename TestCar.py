from car import Car
import PySimpleGUI as sg

# Create a car object
test_car = Car(2020, "Tesla")

# Define the layout of the GUI
layout = [
    [sg.Text("Current Speed: "), sg.Text("0", key="-SPEED-")],
    [sg.Button("Accelerate"), sg.Button("Brake"), sg.Button("Exit")]
]

# Create the GUI window
window = sg.Window("Car Speed", layout)

# Event loop to process GUI events
while True:
    event, values = window.read()

    # Exit the program if the window is closed or the "Exit" button is clicked
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    # Accelerate the car when the "Accelerate" button is clicked
    elif event == "Accelerate":
        for i in range(5):
            test_car.accelerate()
            window["-SPEED-"].update(test_car.get_speed())
            print("Current Speed:", test_car.get_speed())

    # Brake the car when the "Brake" button is clicked
    elif event == "Brake":
        for i in range(5):
            test_car.brake()
            window["-SPEED-"].update(test_car.get_speed())
            print("Current Speed:", test_car.get_speed())

# Close the GUI window
window.close()