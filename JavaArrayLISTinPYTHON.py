# n=int(input())
# for i in range(n):
#     n=list(map(int,input().split()))
n=int(input("enter size: "))
m=[list(map(int,input().split())) for i in range(n)]
answer=[]
for i in range(n):
    l,j=map(int,input().split())
    l=l-1
    j=j-1
    try:
        answer.append(str(m[l][j]))
    except(Exception):
        answer.append("Error")

print('\n'.join(answer))