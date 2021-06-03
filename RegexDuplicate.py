import re
pat=r'\b(\w+)(?:\W\1\b)+'
p=re.compile(pat,re.IGNORECASE)
n=input()
num=p.match(n)
print(re.findall(p.match(n),n))
print(num)