"""Program to sort Python Dictionaries by Key or Value"""

dict1 = eval(input("Enter dict: "))

def sorting_keys(dict1):

    # Sorting by keys
    sorted_dict_by_key = dict(sorted(dict1.items()))
    return sorted_dict_by_key

def sorting_values(dict1):

    # Sorting by values
    sorted_dict_by_values = dict(sorted(dict1.items(), key = lambda x: x[1] ))
    return sorted_dict_by_values

print(f"Sorting by keys: {sorting_keys(dict1)}")
print(f"Sorting by Values: {sorting_values(dict1)}")