"""Program to Display Fibonacci Sequence Using Recursion"""

user_input = int(input("What should be the length of the fibonnaci series: "))

def fibo_recursive(user_input):
    if user_input <=1:
        return user_input
      
    else: 
        
        return fibo_recursive(user_input-1) + fibo_recursive(user_input-2)
        
if user_input<=0:
    print("Enter a positive number")
else:
    for i in range(0,user_input):
        print(fibo_recursive(i))    


            