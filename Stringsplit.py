import re
from typing import Pattern

Pattern=r"[ .,_'?!@]+"
s=input().strip()
print(re.split(Pattern,s))

