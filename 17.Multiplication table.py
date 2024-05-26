#Program to Display the multiplication Table of a table

print("Enter a number to display table")

num = int(input("Enter a number: "))

def table(num):
    result =[]
    for i in range(0,11):
        result.append(f"{num} X {i} = {num*i}")
    return '\n'.join(result)
       
result = table(num)
print(result)
