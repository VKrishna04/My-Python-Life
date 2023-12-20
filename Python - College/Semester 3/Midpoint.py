# Add a method to_polar that will convert the given point X, Y into its equivalent polar co-ordinates form.
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_polar(self):
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        return r, theta


p1 = Point(2, 4)
p2 = Point(4, 6)
print(p1.to_polar())
print(p2.to_polar())
