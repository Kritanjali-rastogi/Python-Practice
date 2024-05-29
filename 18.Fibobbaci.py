# Program to Print the Fibonacci sequence


num = int(input("What should be the length of the fibonaaci series?: "))

def fibo_series(num):
    
    if num==0:
        series = []
    elif num==1:
        series = [0]
    elif num==2:
        series =[0,1]
    else:
        series =[0,1]
        
        for i in range(2,num):
            term = series[i-1] + series[i-2]
            series.append(term)
            

    return series

result = fibo_series(num)
print(result)



