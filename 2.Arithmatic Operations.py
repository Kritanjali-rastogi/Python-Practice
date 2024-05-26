# Program to do arithmatical operations 

list1 = ['Addition', 'Division', 'Substraction', 'Multiplication']
print("Welcome to the basic calulator")

operation = True
while operation not in list1:
    operation = input("What Would you like to perform: Addition, Division, Substraction, or Multiplication? \n")


print("Enter the numbers for which you want to perform the above operation")
num1 = float(input("Enter the first number. Note that this will be the numertaor in case of division: \n"))
num2 = float(input("Enter the second number. Note that this will be the denominator in case of division: \n"))

def calculation(num1,num2):
    
    try: 
        if operation == "Addition":
            return num1 + num2
        elif operation == "Substraction":
            return num1 - num2
        elif operation == "Multiplication":
            return num1 * num2
        elif operation == "Division":
            return num1/num2
        
    except ZeroDivisionError:
        print("Denominator cannot be 0. Please enter another number")

result = (calculation(num1,num2))

if result!= None:
    print(f" The {operation} of the given number results in {result}")