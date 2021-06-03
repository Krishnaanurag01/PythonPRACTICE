import re
n=input()
print(True if (re.match(r'^[a-zA-Z][a-zA-Z0-9_]{7,29}$',n)) else False)