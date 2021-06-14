import re
n="abc@snsnjs.mjmas!mopasj/lpk"
print(re.split(r'[@,./!|\\#^*&`]',n))
print(re.split(r'[^\w]',n))