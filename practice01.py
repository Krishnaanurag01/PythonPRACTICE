n=int(input())
m=input()
l= list(map(str,[i for i in range(n+1)]))
print(l)
total=0
for i in l:
    for j in range(len(i)):
        if(m==i[j]):
            total+=1
print(total)

