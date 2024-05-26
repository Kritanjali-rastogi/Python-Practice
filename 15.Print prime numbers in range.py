# Program to Print all Prime Numbers in an Interval of 1-10000

for num in range(2,10000):

    prime = True

    for i in range(2,num):
        if num%i== 0:
            prime=False
            break
    if prime:
        print(num)
    
    
              
