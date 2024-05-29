# Program to check if a string contains any special character

words = input("Enter a string: ")


def punctuation_check():
     
    list1 = []
    import string
    for item in words:
        if item in string.punctuation:
            list1.append(item)

    return list1

result = punctuation_check()

if result == []:
    print("The string has no special characters")
else:
    print(f"The string has {len(result)} special characters.")