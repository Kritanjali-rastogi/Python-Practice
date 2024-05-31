'''Python program to find second largest number in a list'''

list1 = eval(input("Enter a list: "))

def check(list1):
    a = set(list1)
    b = sorted(list(a),reverse=True)

    second_largest = b[1]
    return second_largest

print(f"The second largest number is: {check(list1)}")