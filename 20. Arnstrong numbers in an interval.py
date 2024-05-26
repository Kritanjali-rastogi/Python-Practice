# Program to Find Armstrong Number in an Interval


num1 = int(input("Enter lower range: "))
num2 = int(input("Enter upper range: "))

def check(num1, num2):

    list1 = []

    for j in range(num1,num2):
                
        sum_cube =0

        for i in str(j):
            i = int(i)   
            sum_cube = sum_cube + (i)**3

        if j == sum_cube:
            list1.append(j)
       
    return list1 
       
result= check(num1, num2)

if result:
    print("Armstrong numbers in the range:", result)
else:
    print("There are no arstrong numbers in this range")  