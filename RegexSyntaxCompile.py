import re

for i in range(int(input())):
    try:
        n=re.compile(input())
        print("Valid")
    except Exception:
        print("Invalid")

