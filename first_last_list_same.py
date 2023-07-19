# Write a program to return True if the first and last number of a given list is same. If numbers are different then return False.
n=input()
list1=n.split()
print(list1)
for i in list1:
    if list1[0]==list1[-1]:
        print("true")
        break
    else:
        print("false")
        break

# Output:
10 20 30 40 10
['10', '20', '30', '40', '10']
true
