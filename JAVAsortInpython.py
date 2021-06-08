n=[tuple(input().split()) for _ in range(int(input()))]

# method-01

# def ss(m):
#     return int(m[1])
# print(sorted(n,key=ss))


# method-02

print(sorted(n,key=lambda x:int(x[1])))