'''Program to find uncommon words from two Strings'''

string_1 = input("Enter string1: ")
string_2 = input("Enter string2: ")

def uncommon(string_1,string_2):
    
    a = set(string_1.split(" "))
    b = set(string_2.split(" "))

    c = a.symmetric_difference(b)

    return list(c)

result = uncommon(string_1,string_2)

print('The uncommon words in both strings are: ')
print(','.join(result))
