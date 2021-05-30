Queue=[]
def insert():
    if n==len(Queue):
        print("Queue is full")
    else:
        Ie=input("Enter number that you wanna add to queue: ")
        Queue.append(Ie)
        print(Queue)
def Delete():
    if not Queue:
        print("Queue is empty")
    else:
        Queue.pop(0)
        print(Queue)
def IS_Empty():
    if len(Queue)==0:
        print("Queue is empty")
def IS_full():
    if n==len(Queue):
        print("Queue is full")

n=int(input("Enter the size of queue:"))
while True:
    print("Choose operations :- 1.Insert 2.Delete 3.IS_Empty 4.Is_full 5.quit")
    oper=int(input())
    if oper == 1:
        insert()
    elif oper == 2:
        Delete()
    elif oper ==3 :
        IS_Empty()
    elif oper == 4:
        IS_full()
    elif oper ==5:
        break
    else:
        print("Enter the correct options !!!")

