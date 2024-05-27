# Program for array rotation

array = eval(input("Enter an array: "))

k = int(input("By how many values would you want to rotate? "))

rotation_type = input("Enter the type of rotation(Left/Right): ")

def rotation(array,k,rotation_type):
    global n
    n = len(array)
    k = k%n
    
    if rotation_type == "Right":
              
        array.reverse()
        array[:k] = reversed(array[:k])
        array[k:] = reversed(array[k:])

        return array    

    elif rotation_type =="Left":
               
        array.reverse()
        array[:(n-k)] = reversed(array[:(n-k)])
        array[(n-k):] = reversed(array[(n-k):])

        return array    


result = rotation(array,k,rotation_type)

print(f"{rotation_type} rotation of array results in {result}")