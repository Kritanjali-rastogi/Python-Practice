# Program to check if given array is Monotonic

# A monotonic array is an array that is either entirely non-increasing or non-decreasing

array = eval(input("Enter an array: "))


def monotonic_check_increasing(array):
    monotonic = True
    
    for i in range(len(array) -1):
        if array[i] > array[i+1]:
            monotonic = False
            break
    
    return monotonic
    
def monotonic_check_decreasing(array):
    monotonic = True
    for i in range(len(array) -1):
        if array[i] < array[i+1]:
            monotonic = False
            break
    return monotonic
    
result = monotonic_check_increasing(array)

if result ==True:
    print(f"The series is a monotonic series")
else:
    result2 = monotonic_check_decreasing(array)
    if result2 == True:
        print(f"The series is a monotonic series")
    else:
        print(f"The series is not a monotonic series")



 