'''Program to find the sum of all items in a dictionary?'''


user_input = eval(input("Enter a dictionary: \n"))

def sum_items(user_input):

    total = 0
    try:
        for value in user_input.values():
            total+= int(value)
    except:
        pass

    return total

result = sum_items(user_input)

print(f"The sum of items in the dictioary is {result}")

