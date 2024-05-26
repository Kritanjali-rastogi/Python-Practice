# Program to Check if a Number is Positive, Negative or Zero

print("Enter a number and we will tell you if it's positive, negative or zero")

num = float(input("Enter a number: "))

def result(num):
    if num==0:
        return "Zero"
    elif num>0:
        return "Positive"
    else:
        return "Negative"
    
final = result(num)

if final == "Zero":
    print(f"The number {num} is 0")
else:
    print(f"The number {num} is a {final} number")