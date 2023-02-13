class Driver:
    def __init__(self, driver_name, drive_speed, car_type):
        self.name = driver_name
        self.speed = drive_speed
        self.car_type = car_type

    def speed_control (self):
        if self.speed >= 110:
            print(self.name, ", car type '", self.car_type, "' must be punished.")
        else:
            print("Great! ", self.name, " is a great driver & He/She should receive a tip.")


Fawad = Driver("Fawad", 100, "BMW")
Fawad.speed_control()

Fahim = Driver("Fahim", 120, "Corolla")
Fahim.speed_control()
