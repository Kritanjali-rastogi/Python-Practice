# check if the given number is a Disarium Number
''' A Disarium number (also known as an Unhappy number) is a number defined by the sum of its 
digits raised to the power of their respective positions'''

num = input("Enter the number whose log you want to find: ")

def check(num):
    total = 0
    j = 1
    for i in num:
        i = int(i)
        D = i**j
        total = total + D
        j = j+1
    return total 

result = check(num)

if result == int(num):
    print(f'{num} is a Disarium number')
else:
    print(f'{num} is a not Disarium number')