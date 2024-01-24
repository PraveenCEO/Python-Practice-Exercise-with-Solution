heights = input("enter the height list").split()
print(heights)
sum=0
count=0
for i in heights:
    count=count+1
for i in heights:
    sum = sum + int(i)
    average = sum/count
print(round(average))

Output:
enter the height list120 130 140 150
['120', '130', '140', '150']
135
