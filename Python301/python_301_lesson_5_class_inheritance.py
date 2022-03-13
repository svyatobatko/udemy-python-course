class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Raawwwwrr")

    def eat(self):
        pass

    def chase(self):
        pass


class Tiger(Animal):
    def speak(self):
        print("They're GREEEEAATTTTTT")


class HouseCat(Animal):

    fur_color = "Black"

    def speak(self):
        print("Meow")


class Dog(Animal):

    fur_color = "White"

    def speak(self):
        print("Wow wow")


tiger = Tiger()
tiger.speak()
cat = HouseCat()
cat.speak()
print(cat.fur_color)
dog = Dog()
dog.speak()
print(dog.fur_color)
