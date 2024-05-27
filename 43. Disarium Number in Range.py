# Program to print all disarium numbers between 1 to 100

list1 = []
for num in range(1,100):
    total = 0
    j =1
    for i in str(num):
        i = int(i)
        D = i**j
        total = total + D
        j = j+1

        if total == num:
            list1.append(num)

print(list1)