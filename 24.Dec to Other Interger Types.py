# Program to Convert Decimal to Binary, Octal and Hexadecimal

l1 = ['Binary','Octal','Hexadecimal']
operation = True
while operation not in l1:
    operation = input("What operation do you want to perform: ")

num = int(input("Enter number that you want to convert to chosen format: "))

def convert(operation, num):
    if operation=="Binary":
        return bin(num)
    elif operation=="Octal":
        return oct(num)
    elif operation=="Hexadecimal":
        return hex(num)
    
result = convert(num)

print(f'The {operation} value of {num} is {result}')

