# Program to find words which are greater than given length k

words = input("Enter comma seprated words: ")

k = int(input("Enter the length: "))

list1 = [x.strip() for x in words.split(',')]

def check(list1,k):
    solution = []
    for item in list1:
        if len(item) > k:
            solution.append(item)
    
    return solution

result = check(list1,k)

print(f"The words that are greater than {k} in length are:")

print(','.join(result))