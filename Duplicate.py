n=input().split()

res=[]

for i in n:
    if(i not in res):
        res.append(i)

print(res)
print(list(dict.fromkeys(n)))

