# Program to check if a given string is binary string or not
# A binary string is a string composed of characters that are either '0' or '1'

words = input("Enter a string: ")

def binary_check(words):
     binary = True
     for item in words:
          if item not in ['0','1']:
               binary = False
     return binary

result = binary_check(words)

if result == True:
     print("The string is a binary string")
else:
     print("The string is not binary")