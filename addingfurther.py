num = list(map(int,input().split()))
for i in range(len(num)-1):
    num[i+1] = num[i] + num[i+1]
print(num)