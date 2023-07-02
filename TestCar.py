from car import Car

#Create a car object
test_car = Car(2020, "Tesla")

#Call the accelerate method 5 times
for i in range(5):
    test_car.accelerate()
    print("Current Speed: ", test_car.get_speed())

#Call the brake method 5 times
for i in range(5):
    test_car.brake()
    print("Current Speed: ", test_car.get_speed())
