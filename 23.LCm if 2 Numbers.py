# Program to Find LCM

num1 = int(input("Enter the first num"))
num2 = int(input("Enter the second num"))

def LCM_Cal(num1,num2):
    HCF = num2
    if num1>num2:
        while num1%num2 !=0:
            num1,num2 = num2,num1%num2
            HCF = num2
        LCM = (num1*num2)/HCF
    elif num1<num2:
        while num2%num1 !=0:
            num2,num1 = num1,num2%num1
            HCF = num1
        LCM = (num1*num2)/HCF
    return LCM 

result = LCM_Cal(num1, num2)
print(f"The HCF of {num1} and {num2} is {result}")
