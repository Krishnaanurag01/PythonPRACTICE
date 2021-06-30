a="aabac"
b="bcaaa"
A=[0 for i in range(256)]
B=[0 for i in range(256)]
# print(int("c"))

for i in a:
    A[ord(i)]+=1

for i in b:
    B[ord(i)]+=1

print(A==B)
    