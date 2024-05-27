# Program to check if the given number is Harshad Number


num = input("Enter a number: ")

def num_check(num):
    digit_sum = 0
    for i in num:
        i = int(i)
        digit_sum +=i

    return digit_sum

result = num_check(num)

if int(num)%result ==0:
    print(f"{int(num)} is a harshad number")
else:
    print(f"{int(num)} is a not harshad number")