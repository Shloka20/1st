#defining variables

weight=input("hey please give your weight in kgs: ")
height=input("hey give your height in meters: ")

BMI=int(weight)/(float(height)*float(height))

if BMI<18.5:
  print("underweight")
elif BMI>25:
  print("overweight")
else:
  print("normal weight")
  
