# Program to Find HCF

num1 = int(input("Enter the first num"))
num2 = int(input("Enter the second num"))

greater_num = max(num1,num2)
smaller_num = min(num1,num2)

def cal_HCF(greater_num, smaller_num):
   
    HCF = smaller_num
    
    while greater_num % smaller_num != 0:
        greater_num = smaller_num
        smaller_num = greater_num//smaller_num
        HCF = smaller_num
    
    return HCF

result = cal_HCF(num1, num2)
print(f"The HCF of {num1} and {num2} is {result}")


           
