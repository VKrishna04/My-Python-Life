# Write a program that has class Cars. Create two objects and set Car1 to be a red convertible with price 10 lakhs and name `Pugo`. Car2 to be a blue sedan named `Mavo` worth 6 lakhs


class Car:
    def __init__(self, colour, type, name, price):
        self.colour = colour
        self.type = type
        self.name = name
        self.price = price

    def display(self):
        print(f"Car name: {self.name}, {self.colour}, {self.type}, {self.price},")


# Create Car1
Car1 = Car("Red", "convertible", "Pugo", "10 lakhs")
Car1.display()
# Create Car2
Car2 = Car("blue", "sedan", "Mavo", "6 lakhs")
Car2.display()
