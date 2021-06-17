# for i in range(1,int(input())+1):
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print(i,end=' , ')




print(*[x for x in range(2, int(input())+1) if all(x % y != 0 for y in range(2, x))])














