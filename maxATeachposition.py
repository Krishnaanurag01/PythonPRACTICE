# num=list(map(int,input().split()))

# l=[]
# m=[]
# f=[]

# for i in num:
#     l.append(i%10)
#     m.append((i//10)%10)
#     f.append((i//100)%10)
# print(l,m,f)

ans=input().split()
a=[max(list(map(int,i))) for i in ans]
print(*a,sep='')

