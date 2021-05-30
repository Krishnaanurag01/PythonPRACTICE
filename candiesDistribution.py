# Q. A teacher has to distrubute candies on the basis of score kids achieve nevertheless each kid will get one candy atleast. and if 
# the kids who has better score than the kids sitting infront and behind in queue then he will get extra candy than those who is sitting behind and infront.
# take input: n= no of students and list=score of students 
# and for further details please watch apni kaksha java series(36th video) 

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

l.sort()
z=0
a=0
for i in range(len(l)):
    if(l[i]>l[i-1]):
        a=a+1
        z=z+a

print(z+len(l))

