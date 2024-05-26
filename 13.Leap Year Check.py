# Program to Check Leap Year

print("Let's check if a year is leap year or not")

year = int(input("Enter a year: "))

def check(year):
    if year%4 ==0:
        return True
    else:
        return False
    
result = check(year)

if result==True:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")