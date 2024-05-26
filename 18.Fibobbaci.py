# Program to Print the Fibonacci sequence


num = int(input("You want to see the fibonacci series of how many terms: "))


def series(num):

    fibonnaci_series = []
    
    for i in range(0,num):
        if i ==0:
            fibonnaci_series.append(0)
        elif i==1:
            fibonnaci_series.append(1)
        else:
            fibonnaci_series.append(fibonnaci_series[i-1]+fibonnaci_series[i-2])
    
    return fibonnaci_series

result = series(num)
print(result)