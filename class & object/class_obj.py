class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type


my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)