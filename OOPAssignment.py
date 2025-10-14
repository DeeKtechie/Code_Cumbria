import math

#Creating a base class

class Shapes:
    def __init__(self):
        pass

    def area(self):
        pass
    def perimeter(self):
        pass

#Creating a child class for Circle

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

#Creating a child class for Rectangle
class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

#Creating a child class for Equilateral Triangle
class Triangle(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * (self.side ** 2)

    def perimeter(self):
        return 3 * self.side
    

#Test Code
if __name__ == "__main__":
    # Circle
    circle = Circle(5)
    print("Circle:")
    print(f" Radius: {circle.radius}")
    print(f" Area: {circle.area():.2f}")
    print(f" Perimeter: {circle.perimeter():.2f}\n")

    # Rectangle
    rectangle = Rectangle(6, 4)
    print("Rectangle:")
    print(f" Length: {rectangle.length}, Width: {rectangle.width}")
    print(f" Area: {rectangle.area():.2f}")
    print(f" Perimeter: {rectangle.perimeter():.2f}\n")

    # Equilateral Triangle
    triangle = Triangle(5)
    print("Equilateral Triangle:")
    print(f" Side: {triangle.side}")
    print(f" Area: {triangle.area():.2f}")
    print(f" Perimeter: {triangle.perimeter():.2f}")