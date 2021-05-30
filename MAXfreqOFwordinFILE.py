
file =open('gfg.txt','r')

line_word=[i.lower().replace(',','').replace('.','').split() for i in file]
words=[k for j in line_word for k in j]
freq=0
stringIS=""
for w in range(len(words)):
    count=1
    for j in range(w+1,len(words)):
        if(words[w]==words[j]):
            count=count+1
    if(count>freq):
        freq=count
        stringIS=words[w]

print(f"Most Common word is : {stringIS} and  Frequency is {freq}")
file.close()



