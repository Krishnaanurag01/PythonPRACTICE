Stack=[]
def push():
    if(len(Stack)==n):
        print("Stack Overflow")
    else:
        e=int(input("Enter the Element that you wanna push: "))
        Stack.append(e)
        print(Stack)
def pop():
    if(len(Stack)<=0):
        print("Stack underflow")
    else:
        Stack.pop()
        print(Stack)
def peek():
    print(f"Top element is {Stack[-1]}")

n= int(input("Enter the size of stack : "))

while True:
    print("Choose operations : 1. push 2.pop 3.peek 4.quit")
    m=int(input())
    if m==1:
        push()
    elif m==2:
        pop()
    elif m==3:
        peek()
    elif m==4:
        break
    else:
        print("Enter the correct options !!!")
