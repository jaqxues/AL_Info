weight = float(input("Weight: "))
height = float(input("Height: "))

bmi = weight / (height ** 2)
print("BMI:", bmi)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("healthy weight")
elif bmi < 30:
    print("overweight")
else:
    print("obese")
