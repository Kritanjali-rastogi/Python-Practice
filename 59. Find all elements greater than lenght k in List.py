# Program to find words which are greater than given length k

list1 = eval(input("Enter a list: "))

k = int(input("Enter the length: "))

def check(list1,k):
    solution = []
    for item in list1:
        if len(item) > k:
            solution.append(item)
    
    return solution

result = check(list1,k)

print(f"The words that are greater than {k} in length are:")

for item in result:
    print(item)