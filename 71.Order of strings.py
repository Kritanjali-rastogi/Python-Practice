from collections import OrderedDict, Counter

def check_order(string):
    # Create an OrderedDict with character counts
    ordered_dict = OrderedDict(Counter(string))

    # Compare the original string with the keys of the OrderedDict
    # If they match, the order is preserved
    return string == ''.join(ordered_dict.keys())

# Example usage
input_string = "hello"
result = check_order(input_string)
print("Order preserved:", result)