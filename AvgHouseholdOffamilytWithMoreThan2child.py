n = int(input())
incomeList = [int(input()) for _ in range(n)]
childrensList = [int(input()) for _ in range(n)]

total = 0
count = 0
for i in range(n):
    if(childrensList[i] > 2):
        total += incomeList[i]
        count+=1

print(f"Avg income is : {total//count}")