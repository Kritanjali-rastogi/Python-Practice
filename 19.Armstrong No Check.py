# Program to Check Armstrong Numb
# Armstrong number is a number that is equal to the sum of cubes of its digits

print("Let's check if the a number is armstrong")

num = input("Enter a number: ")

def check(num):
    sum_cube =0   
    for i in num:
        digit_cube = int(i)**3
        sum_cube += digit_cube
    return sum_cube
    
result= check(num)

if result==int(num):
    print(f"The number {num} is an armstrong number")
else:
    print(f"The number {num} is not an armstrong number")    
    
