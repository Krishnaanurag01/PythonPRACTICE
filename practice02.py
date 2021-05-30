numbers=list(map(int,[input() for i in range(3)]))
last=[]
mid=[]
first=[]
# for i in numbers: 
#     last.append(i[-1])
#     mid.append(i[-2])
#     first.append(i[-3])

# first.sort(reverse=True)
# mid.sort(reverse=True)
# last.sort(reverse=True)

# print(f"{first[0]}{mid[0]}{last[0]}")



for i in numbers:
    last.append(i%10)
    mid.append((i//10)%10)
    first.append((i//100)%10)

print(f"{max(first)}{max(mid)}{max(last)}")
