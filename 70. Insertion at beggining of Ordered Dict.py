'''Program to insertion at the beginning in OrderedDict'''

from collections import OrderedDict

ordered_dict = OrderedDict(eval(input("Enter initial Dict: ")))
new_key = input("Enter new key: ")
new_keyvalue = input("Enter new key-value: ")

def insertion(ordered_dict,new_key,new_keyvalue):
    ordered_dict[new_key]=new_keyvalue
    ordered_dict.move_to_end(new_key,last = False)

    return ordered_dict

print(insertion(ordered_dict,new_key,new_keyvalue))