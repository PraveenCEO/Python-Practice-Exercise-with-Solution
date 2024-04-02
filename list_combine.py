'''Create a new list from two list using the following condition
Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.'''
list1 = []
list2 = []
new_list = []
n = int(input("Enter the elements to be added in the list: "))
print("Enter List1: ")
for i in range(n):
    element1 = int(input())
    list1.append(element1)
print(list1)

for i in range(n):
    if list1[i] % 2 != 0:
       print(list1[i])
       new_element = list1[i]
       new_list.append(new_element)
print(new_list)

print("Enter List2: ")
for j in range(n):
      element2 = int(input())
      list2.append(element2)
print(list2)

for j in range(n):
    if list2[j] % 2 == 0:
       print(list2[j])
       new_element = list2[j]
       new_list.append(new_element)
print("The new list is:",new_list)

'''
Output:
Enter the elements to be added in the list: 5
Enter List1: 
10 
20
25
30
35
[10, 20, 25, 30, 35]
25
35
[25, 35]
Enter List2: 
40
45
60
75
90
[40, 45, 60, 75, 90]
40
60
90
The new list is: [25, 35, 40, 60, 90]
'''
