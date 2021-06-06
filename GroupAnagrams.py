from collections import defaultdict

n=['eat','tea','ate','hey','yeh','hum','muh','huh','hhu']

ans=defaultdict(list)
for i in n:
    a=''.join(sorted(i))
    ans[a].append(i)

for i in ans.values():
    print(i)
