from itertools import product

n=[int(input()) for i in range(int(input()))]
for i in range(len(n)):
    sum=0
    for j in range(i,len(n)):
        sum+=n[j]
        if(sum==0):
            print("Found it !")
