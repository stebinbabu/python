x=int(input("Enter the side of square:"))
area=lambda x:x*x
print("Area of square:{0}".format(area(x)))
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the bredth of the rectangle:"))
area=lambda l,b:l*b
print("Area of the triangle:{0}".format(area(l,b)))
b=int(input("Enter the bredth of the triangle:"))
h=int(input("Enter the hight of the triangle:"))
area=lambda b,h:0.5*b*h
print("Area of the triangle:{0}".format(area(b,h)))

