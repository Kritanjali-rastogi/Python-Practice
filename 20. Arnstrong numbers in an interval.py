# Program to Find Armstrong Number in an Interval


range1 = input("Enter range in comma separted sequence: ")
l1 = range1.split(",")
lower_range = int(l1[0])
upper_range = int(l1[1])

def check(lower_range,upper_range):

    list1 = []

    for num in range(lower_range,upper_range):
               
        sum_cube =0
        for i in str(num):
            sum_cube = sum_cube + int(i)**3

        if num == sum_cube:
            list1.append(num)
       
    return list1 
       
result= check(lower_range,upper_range)

if result:
    print("Armstrong numbers in the range:", result)
else:
    print("There are no arstrong numbers in this range")  