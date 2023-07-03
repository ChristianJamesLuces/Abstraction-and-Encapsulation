from fan import Fan

#Create the objects
fan1 = Fan(Fan.FAST, 10, "yellow", True)
fan2 = Fan(Fan.MEDIUM, 5, "blue", False)
    
#Display the properties of fan1
print("Fan 1: ")
print("Speed: ", fan1.get_speed())
print("Radius: ", fan1.get_radius())
print("Color: ", fan1.get_color())
print("On: ", fan1.get_on())

#Display the properties of fan2
print("\nFan 2: ")
print("Speed: ", fan2.get_speed())
print("Radius: ", fan2.get_radius())
print("Color: ", fan2.get_color())
print("On: ", fan2.get_on())