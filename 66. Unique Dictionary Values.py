'''Program to Extract Unique values dictionary values'''


user_input = eval(input("Enter a dictionary:\n"))

def unique_values(user_input):
    
    unique = set()
    for value in user_input.values():
        unique.add(str(value))

    return unique

result = unique_values(user_input)

print("The unique values in the dictionary are: ")
print(' '.join(list(result)))