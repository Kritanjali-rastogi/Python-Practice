# Program to print all disarium numbers between 1 to 100

list1= []
for i in range(1,100):
    i = str(i)
    total = 0
    for j in range(len(i)):
        b = int(i[j])**(j+1)
        total+=b

    if total ==int(i):
        list1.append(int(i))
print(list1)