# Enter your code here. Read input from STDIN. Print output to STDOUT
def checker():
    n=int(input())
    ns=set(map(int,input().split(' ')))
    n1=int(input())
    ns1=set(map(int,input().split(' ')))
    answer=True
    for i in ns:
        answer=False
        if i in ns1:
            answer=True
    print(answer)
    
for i in range(int(input())):
    checker()
            
