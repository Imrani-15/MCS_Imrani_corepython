#  square and cube symbol in the area of a rectangle and volume of a cylinder
def cube(val):
    return (val*val*val)
def square(val):
    return (val*val)

val = int(input("Enter the Number:"))
print("Cube value is: ",cube(val))
print("Square value is: ",square(val))


area = 1256.66
volume = 1254.725
decimal = 2
print("The area of the rectangle {0:.{1}f}cm\u00b2".format(area,decimal))
decimal = 3
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume,decimal))
