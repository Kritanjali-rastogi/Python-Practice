# Program to do arithmatical operations 


print("Welcome to the basic calulator")

list1 = ['addition', 'substraction', 'multiplication', 'division']

operation = ''
while operation.lower() not in list1:
    print("Enter the operation correctly")
    operation = input("Enter one: Addition, Substraction, Multilpication, Division: \n")

print("Enter the numbers for which you want to perform the above operation")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


def calculator(num1,num2,operation):
    try:
        if operation.lower() == "addition":
            return num1+num2
        elif operation.lower() == "substraction":
            return num1-num2
        elif operation.lower() == "multiplication":
            return num1*num2
        elif operation.lower() == "division":
            return num1/num2
    except ZeroDivisionError:
        print("Denominator cannot be 0. Enter a different second number")

result = calculator(num1,num2,operation)

if result!= None:
    print(f"The {operation.lower()} of the numbers returns {result}")