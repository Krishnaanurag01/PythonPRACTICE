# # # Enter your code here. Read input from STDIN. Print output to STDOUT
# # en=int(input())
# # enli=set([int(x) for x in input().split()])
# # fr=int(input())
# # frli= set([int(y) for y in input().split()])

# # print(enli-frli)

# # A = [1,2,3]
# # B = [6,5,4]
# # C = [7,8,9]
# # X = [A] + [B] + [C]
# # print(X)
# # n=zip(*X)
# # for i in n:
# #     print(i)
# x,k=map(int,input().split())
# # p=input()
# print(eval(input())==k)

# def fibonacci(n):
#     a=0
#     b=1
#     num=[]
#     if n==1:
#         return a
#     elif n==2:
#         return [a,b]
#     else:
#         num.append(a)
#         num.append(b)
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             num.append(c)
#     return num

# print(fibonacci(1))
def keywordExample(x=1, y=2, z=4):
    sum = x+y
    min = sum - z
    print (min)
keywordExample(y=8,x=4,z=y)