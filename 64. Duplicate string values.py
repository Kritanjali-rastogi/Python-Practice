'''Program to find all duplicate characters in string'''

user_input = input("Enter a string: ")

def check(user_input):
    char_count = {}
    for i in user_input.split(' '):
        if i in char_count:
            char_count[i]+=1
        else:
            char_count[i] = 1

    duplicate = []
    for word, number in char_count.items():
        if number > 1:
                duplicate.append(word)

    return duplicate

result = check(user_input)

print("The duplicate words in the string are: ")
print(" ".join(result))