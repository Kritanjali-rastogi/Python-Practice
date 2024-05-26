# Program to Find the Sum of Natural Numbers

num = int(input("For how many natural numbers would you want to calculate the sum?: "))

def sum_cal(num):
    sum = (num * (num+1))/2
    return sum

result = sum_cal(num)
print(f"The sum of first {num} natural numbers is {result}")
