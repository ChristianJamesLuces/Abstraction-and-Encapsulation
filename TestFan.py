import PySimpleGUI as sg
from fan import Fan

# Create the fan objects
fan1 = Fan(Fan.FAST, 10, "yellow", True)
fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

# Define the layout for the GUI
layout = [
    [sg.Text("Fan 1 Properties")],
    [sg.Text("Speed:"), sg.InputText(str(fan1.get_speed()))],
    [sg.Text("Radius:"), sg.InputText(str(fan1.get_radius()))],
    [sg.Text("Color:"), sg.InputText(str(fan1.get_color()))],
    [sg.Checkbox("On", default=fan1.get_on())],
    [sg.Text("Fan 2 Properties")],
    [sg.Text("Speed:"), sg.InputText(str(fan2.get_speed()))],
    [sg.Text("Radius:"), sg.InputText(str(fan2.get_radius()))],
    [sg.Text("Color:"), sg.InputText(str(fan2.get_color()))],
    [sg.Checkbox("On", default=fan2.get_on())]
]

# Create the window
window = sg.Window("Fan Properties", layout)

# Event loop to process GUI events
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

# Close the window
window.close()