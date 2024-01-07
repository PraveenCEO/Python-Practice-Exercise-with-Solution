weight = input("Enter weight in kilograms: ")
height = input("Enter height in meters: ")

# Convert inputs to float
weight = float(weight)
height = float(height)

# Calculate BMI
bmi = weight / (height ** 2)

# Print the result
print("BMI:", bmi)
