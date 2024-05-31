# Program for removing i-th character from a string


words = input("Enter a string: ")
k = int(input("Which character do you want to remove?: "))



def char_removal(words,k):
    
    if k < 1 or k > len(words):
        return words
    else:
        modified_words = words[:k-1] + words[k:]
        
        return modified_words

result = char_removal(words,k)

print(result)