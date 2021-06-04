l=[int(x) for x in input().split()]
# for i in range(len(data)):
#     for j in range(len(data)-1):
#         if data[j+1]<data[j]:
#             data[j+1],data[j]=data[j],data[j+1]
# print(data)

def swap(a,b):
    a,b=b,a
    return a,b 


# ans=[[swap(data[j+1],data[j]) for j in range(len(data)-1) if data[j+1]<data[j] ] for i in range(len(data))]
def bubblesort(l):
    [l.append(l.pop(0) if i == len(l) - 1 or l[0] < l[1] else l.pop(1)) for j in range(0, len(l)) for i in range(0, len(l))]
    return l
print(bubblesort(l))