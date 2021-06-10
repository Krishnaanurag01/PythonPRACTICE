# sum=0
# for i in range(1,n+1):
#     if n%i==0:
#         sum+=i
# print(sum)




n=int(input())
l=[i for i in range(1,n+1) if n%i==0]
print(sum(l))
