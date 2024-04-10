Dict={}
n=int(input())
for i in range(1,n+1):
    key=int(input())
    values=key*key
    Dict[key]=values
print(Dict)

'''
Output:
8
1
2
3
4
5
6
7
8
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
