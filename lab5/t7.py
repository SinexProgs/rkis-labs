x = float(input("Enter X coordinate of a point: "))
y = float(input("Enter Y coordinate of a point: "))
radius = float(input("Enter radius of a circle: "))

print("Point is in the circle" if x * x + y * y < radius * radius else "Point is outside of the circle")