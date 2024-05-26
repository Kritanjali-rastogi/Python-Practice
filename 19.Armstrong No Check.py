# Program to Check Armstrong Numb
# Armstrong number is a number that is equal to the sum of cubes of its digits

print("Let's check if the a number is armstrong")

num = input("Enter a number: ")

def check(num):
    sum_cube =0   
    for i in num:
        i = int(i)
        sum_cube = sum_cube + (i)**3

    if int(num) == sum_cube:
        return True
    else:
        return False
    
result= check(num)
if result==True:
    print(f"The number {num} is an armstrong number")
else:
    print(f"The number {num} is not an armstrong number")    
    
