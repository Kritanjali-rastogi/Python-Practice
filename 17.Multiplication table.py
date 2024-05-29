#Program to Display the multiplication Table of a table

print("Enter a number to display table")

num = int(input("Enter a number: "))

def table_cal(num):
    table =[]
    for i in range(0,11):
        table.append(f"{num} X {i} = {num*i}")
    return table
       
result = table_cal(num)
print("\n".join(result))
