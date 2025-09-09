class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return self.name + ": " + "Woof!"


class Cat(Animal):
    def speak(self):
        return self.name + ": " + "Meow!"


pies = Dog("Pies")
kot = Cat("Kot")

print(pies.speak())
print(kot.speak())
