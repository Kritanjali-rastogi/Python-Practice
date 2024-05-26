# Program to solve quadratic equation


print("Let's solve a quadratic equation")
print(" ")
print("Quadratic equation is of the form ax²+bx+c=0, where a, b, and c are coefficients")
print("To solve it, we plug these coefficients in the formula: (-b±√(b²-4ac))/(2a)")
print(" ")
print("You need to provide all the coefficients in the next steps")
print(" ")

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

discriminant = (b**2)-(4*a*c)

import math
def solution(a,b,c,discriminant):

    if discriminant >=0:
        first_solution = (-b + math.sqrt(discriminant))/(2*a)
        second_solution = (-b - math.sqrt(discriminant))/(2*a)
        return first_solution, second_solution
    else:
        return None

result = solution(a,b,c,discriminant)

print(" ")
if result == None:
    print("The values of a,b, and c enetered by you do not make a valid quadratic equation")
else:
    print(f"The roots of the equation are: {result}")

