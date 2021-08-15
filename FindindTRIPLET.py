from itertools import product
li=[8,3,4,5]
li02=[2,3,-7,5]
li00=[0,-1,4,9]

num=product(li,li02,li00)

for i in num:
    if sum(i)==0:
        print("Sum of {} is 0".format(i))
        