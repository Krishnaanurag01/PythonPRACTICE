
def add(*args):
    total=0
    for i in args:
        total+=i
    return total

print(add(2,3,4))
print(add(2,3,4,9,4,2,4))
print(add(2,3))
print(add(2,3,4,5))

