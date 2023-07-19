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