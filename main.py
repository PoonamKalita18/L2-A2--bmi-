h = float(input("enter your heigth :"))
w = float(input("enter your weight :"))
BMI = w/(h/100)**2
print("your BMI is :", BMI)

if BMI <=18.4:
    print("you're underweight")
elif BMI <=24.9:
    print("you're healthly")
elif BMI <=29.9:
    print("you're overweight")
elif BMI <=34.9:
    print("you're severly overweight")
elif BMI <=39.9:
    print("you're obese")
else:
    print("you are severly obese!!!!")