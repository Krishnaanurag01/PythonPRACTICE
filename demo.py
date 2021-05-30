# Enter your code here. Read input from STDIN. Print output to STDOUT
from typing import Collection


from collections import Counter
x=int(input())
m=[int(i) for i in input().split()]
nc=int(input())
temp=[]
for _ in range(nc):
    temp.append(list(map(int,input().split())))
counterx=Counter(m)
print(counterx)
# for i in temp:
#     if counterx.
    