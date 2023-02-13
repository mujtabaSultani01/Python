# Inheritance is the procedure in which one class inherits the attributes and methods of another class.
class Vehicle:
    def general_usage(self):
        print("General usage: Transportation")


class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.has_roof = True
        print("I'm Car. I've", self.wheels, "wheels and a roof.")

    def specific_usage(self):
        print("I can be used for common transportation or for family vacation.")


class Motorcycle (Vehicle):
    def __init__(self):
        self.wheels = 2
        self.has_roof = False
        print("I'm Motorcycle. I've", self.wheels, "wheels and no roof.")

    def specific_usage(self):
        print("I can be used for road driving or racing.")


car = Car()
car.general_usage()
car.specific_usage()

motorcycle = Motorcycle()
motorcycle.general_usage()
motorcycle.specific_usage()

# isinstance() method can be used to check whether an object is an instance of a specific class or no.
# issubclass() method can be used to check whther a class is sub class of other class or no.

print("is motorcycle object is an instance of Car class?", isinstance(motorcycle, Car))
print("is Car a sub class of Vehicle class?", issubclass(Car, Vehicle))
