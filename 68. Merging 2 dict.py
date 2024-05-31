'''Program to Merge two Dictionaries'''

dict_1 = eval(input("Enter dict 1: "))
dict_2 = eval(input("Enter dict 2: "))

def merging_dict(dict_1,dict_2):
    dict_1.update(dict_2)

    return dict_1


result = merging_dict(dict_1,dict_2)

print(result)

