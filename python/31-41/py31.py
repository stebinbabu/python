
from graphics import circle, rectangle
from graphics.dgraphics import cuboid, sphere

r = int(input("Enter the radius of circle:"))
circle.areac(r)
circle.peric(r)
l = int(input("Enter the length of rectangle:"))
b = int(input("Enter the breadth of rectangle:"))
rectangle.arear(l, b)
rectangle.perir(l, b)
l1 = int(input("Enter the length of cuboid:"))
b1 = int(input("Enter the breadth of cuboid:"))
h1 = int(input("Enter the height of cuboid:"))
cuboid.areacub(l1, b1, h1)
cuboid.pericub(l1, b1, h1)
r1 = int(input("Enter the radius of sphere:"))
sphere.areas(r1)
sphere.peris(r1)
graphics
circle.py


def areac(r):
    a = 3.14 * r * r


print("Area of Circle is:", a)


def peric(r):
    p = 2 * 3.14 * r
    print("Perimeter of Circle is:", p)


rectangle.py


def arear(l, b):
    a = l * b
    print("Area of Rectangle is:", a)


def perir(l, b):
    p = 2 * (l + b)
    print("Area of Rectangle is:", p)


dgraphics
sphere.py


def areas(r):
    a = 4 * 3.14 * r * r
    print("Area of Sphere is:", a)


def peris(r):
    p = 6.2832 * r
    print("Perimeter of Sphere is:", p)


cuboid.py


def areacub(l, b, h):
    a = 2 * ((l * b) + (b * h) + (h * l))
    print("Area of Cuboid is:", a)


def pericub(l, b, h):
    p = 4 * (l + b + h
    print("Perimeter of Cuboid is:", p)

