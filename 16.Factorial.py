# Program to Find the Factorial of a Number

print("Enter a number to calculate factorial")

num = int(input("Enter a number: "))


def factorial(num):
    i = 1
    fac = 1
    if num==1 or num==0:
        return 1
    else:
        while i <=num:
            fac = fac*i
            i +=1
        return fac

result = factorial(num)

print(f"The factorial of the number is: {result}")
