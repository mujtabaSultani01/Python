"""
Multiple inheritance is a feature of some object-oriented computer programming languages in which an object or class
can inherit features from more than one parent object or parent class.
"""


class Father:
    def gardening(self):
        print("I love gardening...")


class Mother:
    def teaching(self):
        print("I love teaching...")


class Child(Father, Mother):
    def sporting(self):
        print("I love playing cricket.")


ch = Child()
ch.gardening()
ch.teaching()
ch.sporting()


# in other way:

class Father1:
    def skills(self):
        print("I love gardening and walking")

class Mother1:
    def skills(self):
        print("I love teaching and art.")

class Child1 (Father1, Mother1):
    def sporting(self):
        Father1.skills(self)
        Mother1.skills(self)
        print("I love playing Volleyball.")


ch1 = Child1()
ch1.sporting()