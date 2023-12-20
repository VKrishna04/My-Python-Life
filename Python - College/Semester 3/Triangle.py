# Make a class triangle. Enter its three sides and calculate its area.
import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        s = (a + b + c) / 2
        self.area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    def display(self):
        print(
            f"The area of the triangle of sides {self.a}, {self.b}, {self.c} is {self.area}"
        )


a = int(input("Please enter the length of side a: "))
b = int(input("Please enter the length of side b: "))
c = int(input("Please enter the length of side c: "))
tri1 = Triangle(a, b, c)
tri1.display()
