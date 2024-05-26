# Program to convert kilometres to miles

# Input from user
Distance = eval(input("Enter the distance in kilometers: "))
Conversion_factor = 0.621371

# Function

def km_to_miles(Distance):

       D = Distance*Conversion_factor
       return D

result = km_to_miles(Distance)
print(f"{Distance} kms is {result} miles")