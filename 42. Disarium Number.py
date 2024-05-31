# check if the given number is a Disarium Number
''' A Disarium number (also known as an Unhappy number) is a number defined by the sum of its 
digits raised to the power of their respective positions'''

a = int(input("Enter no: "))

def check(a):
    a =str(a)    
    sum = 0
    for i in range(len(a)):
        b = int(a[i])**(i+1)
        sum+=b
    return sum

result = check(a)

if result==a:

    print("True")
else: 
    print("False")