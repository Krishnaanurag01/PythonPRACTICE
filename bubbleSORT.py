data=[int(x) for x in input().split()]


# print(data)
# data[0]=9
# print(data)



temp=0
for i in range(len(data)):
    for j in range(len(data)-1):
        if data[j+1]<data[j]:
            temp=data[j+1]
            data[j+1]=data[j]
            data[j]=temp
print(data)


