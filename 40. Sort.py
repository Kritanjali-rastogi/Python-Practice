# Program to Sort Words in Alphabetic Order

string = input("Enter a string: ")

def string_sorting(string):
    words = string.split()
    sorted_words = sorted(words)
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence

result = string_sorting(string)

print({result})