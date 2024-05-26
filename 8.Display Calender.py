# Program to display calendar


import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1 to 12): "))

def calender(year, month):
    return calendar.month(year, month)

result = calender(year, month)

print(result)