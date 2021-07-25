num = list(map(int,input().split()))
uniquenum=[]
for i in num : 
    if i not in uniquenum:
        uniquenum.append(i)

print(uniquenum)

