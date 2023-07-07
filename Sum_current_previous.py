# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
previous_num=0
for i in range(1,11):
    print("Current number",i,"previous num",previous_num, "Sum:",(i+previous_num))
    previous_num=i
