# Program to Check Prime Number

num = int(input("Enter a number: "))



def prime_check(num):
    prime = True
    for i in range(2,num):
        if num%i==0:
            prime = False
            break
                           
    return prime

result = prime_check(num)

if result==True:
    print("The number is prime")
else:
    print("The number is not prime")