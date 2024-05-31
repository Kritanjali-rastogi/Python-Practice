"""Program to convert key-values list to flat dictionary"""

user_input = eval(input("Enter a list: "))

def dict_return(user_input):
    key_values = []
    value_values = []
    
    for i in range(len(user_input)):
        for j in range(len(user_input[i])):
            if ((user_input[i])[j]) == ':':
                key_values.append((user_input[i][:j]))
                value_values.append((user_input[i][(j+1):]))

    dict1= {}

    for i in range(len(key_values)):
        for j in range(len(value_values)):
            if i==j:
                dict1[key_values[i]] = value_values[j]
        
    return dict1

result  = dict_return(user_input)

print(result)
