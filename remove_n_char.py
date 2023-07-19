# Write a program to remove characters from a string starting from zero up to n and return a new string.
str1=str(input("Enter any text to remove first n:"))
x=int(input("Enter the length to remove first n number:"))
n=str1[x:]
print("After removing character from string:",n)
