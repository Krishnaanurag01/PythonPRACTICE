l1=[3,0,1,-1,2,-3]

for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        for k in range(j+1,len(l1)):
            if(l1[i]+l1[j]+l1[k]==0):
                print(f"{l1[i]}+{l1[j]}+{l1[k]} is Triplet")
            else:
                False