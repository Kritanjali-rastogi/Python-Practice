# Program to find the area of a triangle
# Area of a triagle = 1/2 * Base * Height

print("Let's calculate the area of a triangle")
print(" ")

base = float(input("Enter the lenght of the triagles's base (in cm): "))
print(" ")
height = float(input("Enter the height of the triagles (in cm): "))

def area(base, height):
    A = 1/2 * base * height
    return A

result = area(base, height)
print(f"The area of the triagle with base {base} cm and height {height} cms is {result} cm2")