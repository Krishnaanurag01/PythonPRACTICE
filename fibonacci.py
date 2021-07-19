n = int(input("Enter number : "))

def fibonacci(num):
    a=0
    b=1
    if num == 0 :
        print("Incorrect")
    if num ==1:
        print(a)
    elif num == 2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(num-2):
            c=a+b
            a=b
            b=c
            print(c,end=" ")

fibonacci(n)

            
