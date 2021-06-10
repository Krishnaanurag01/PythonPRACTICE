from itertools import permutations
n="abs"
for i in permutations(n,3):
    print(''.join(i))