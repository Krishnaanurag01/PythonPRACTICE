n=list(map(int,input().split()))
size=int(input("size"))
answer=[]
for i in range(len(n)):
    z=n[i:i+size]
    if(len(z)==size):
        answer.append(max(n[i:i+size]))
print(*answer)