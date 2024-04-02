#Palindrome Number
num=int(input())
num1=str(num)
rev=str(num1)[::-1]
print(rev)
if num1==rev:
    print("palindrome")
else:
    print("not palindrome")

#Palindrome both string and Number
str1=input()
rev=str1[::-1]
print(rev)
if str1==rev:
    print("palindrome")
else:
    print("not palindrome")
