# BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in metres squared

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))


def calculate_BMI(weight, height):
    BMI = (weight/(height**2))
    return BMI

result = calculate_BMI(weight, height)

if result >= 30.0:
    print(f"Your BMI is {result}. You are obese")
elif 25.0 <= result <= 29.9:
    print(f"Your BMI is {result}. You are overweight")
elif 18.5 <= result <= 24.9:
    print(f"Your BMI is {result}. You have a healthy weight")
else:
    print(f"Your BMI is {result}. You are underweight")