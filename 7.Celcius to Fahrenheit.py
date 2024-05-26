# Program to convert Celsius to Fahrenheit

print("Let's convert celcius to fahrenheit")

celcius = float(input("Enter the tempertaure in degree celcius: "))

def Cel_to_fah(celcius):
    T = ((celcius)*9/5) + 32
    return T

result = Cel_to_fah(celcius)
print(f"{celcius} degree celcius is {result} degree fahrenheit")