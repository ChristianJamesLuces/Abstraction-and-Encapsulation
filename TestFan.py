import PySimpleGUI as sg
from fan import Fan

# Create the fan objects
fan1 = Fan(Fan.FAST, 10, "yellow", True)
fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

# Define the table headings and data for fan properties
table_headings = ["Fan", "Speed", "Radius", "Color", "On"]
table_data = [
    ["Fan 1", str(fan1.get_speed()), str(fan1.get_radius()), str(fan1.get_color()), str(fan1.get_on())],
    ["Fan 2", str(fan2.get_speed()), str(fan2.get_radius()), str(fan2.get_color()), str(fan2.get_on())]
]

# Define the layout for the GUI
layout = [
    [sg.Table(values=table_data, headings=table_headings, justification="center", key="-TABLE-", num_rows=2)],
    [sg.Button("Exit")]
]

# Create the window
window = sg.Window("Fan Properties", layout)

# Event loop to process GUI events
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

# Close the window
window.close()