# Program for cube sum of first n natural numbers
# S = [n2 (n + 1)2]/4, where S is the sum and n is the number of natural numbers taken

num = int(input("For how many natural numbers would you want to calculate the sum of cube?: "))

def cal_cube_sum(num):
    S = ((num **2) * (num + 1)**2)/4
    return S

result = cal_cube_sum(num)

print(f"The sum of cube of first {num} natural numbers is {result}")