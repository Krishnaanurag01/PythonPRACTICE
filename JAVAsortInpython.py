n=[input().split() for _ in range(int(input()))]

def ss(m):
    return int(m[2])
print(sorted(n,key=ss))

# print(sorted(n,key=ss))