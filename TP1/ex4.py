import math
a = int(input("Type the value of A: "))
b = int(input("Type the value of B: "))

print(f"Perimeter: {2*(a + b)}")
print(f"It is {'a' if a == b else 'not a'} square")
print(f"The length of the diameter is {math.sqrt(a**2+b**2)}") # fix

R=int(input("Enter the radius of the cylinder"))
print(f"The volume of the cylinder is {math.pi*a*R**2}")
