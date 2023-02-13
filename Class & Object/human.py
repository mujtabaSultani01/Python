# Class is an abstraction of some entities which contains common properties and methods.

# Python class section:
class Human:
    def __init__(self, person_name, person_occupation):
        self.name = person_name
        self.occupation = person_occupation

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, " Plays tennis.")
        elif self.occupation == "class teacher":
            print(self.name, " teaches well.")

    def do_speak(self):
        print("How are you", self.name, "?")


# End of python class.

# Python object starts here.

Ahmad = Human("Faisal", "tennis player")
Ahmad.do_work()
Ahmad.do_speak()

Sana = Human("Sana", "class teacher")
Sana.do_work()
Sana.do_speak()

# End of python object.
