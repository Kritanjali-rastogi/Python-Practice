'''Python program to find N largest number in a list'''

list1 = eval(input("Enter a list: "))

k = int(input("How many largest numbers do you want: "))

def check(list1,k):
    a = set(list1)
    b = sorted(list(a),reverse=True)

    return b[0:k]

print(f"{k} largest numbers in the list are: ")
print(check(list1,k))