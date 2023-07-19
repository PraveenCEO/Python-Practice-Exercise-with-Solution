# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
previous_num=0
for i in range(1,11):
    print("Current number",i,"previous num",previous_num, "Sum:",(i+previous_num))
    previous_num=i

# Output:
Current number 1 previous num 0 Sum: 1
Current number 2 previous num 1 Sum: 3
Current number 3 previous num 2 Sum: 5
Current number 4 previous num 3 Sum: 7
Current number 5 previous num 4 Sum: 9
Current number 6 previous num 5 Sum: 11
Current number 7 previous num 6 Sum: 13
Current number 8 previous num 7 Sum: 15
Current number 9 previous num 8 Sum: 17
Current number 10 previous num 9 Sum: 19
