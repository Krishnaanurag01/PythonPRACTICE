n=int(input())
sizeL=int(input())
l=[]
for i in range(0,n):
    l.append(input().split())


for i in l:
    for j in range(0,len(i)):
        for k in range(1,len(i)):
            for m in range(2,len(i)):
                if(i[j]+i[k]+i[m]==0):
                    print("1")
                else:
                    print("not zero")
