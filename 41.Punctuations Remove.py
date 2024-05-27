# Program to Remove punctuation from a String

import string

string_1 = input("Enter a string: ")

def punctuation_remove(string_1):
    result = ''
    for i in string_1:
        if i not in string.punctuation:
            result += i
    return result

final = punctuation_remove(string_1)

print(final)