class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
    
    def AddLast(self,data):
        newnode=node(data)
        if(self.head is None):
            self.head=newnode
            return
        temp=self.head
        while(temp.next!= None):
            temp=temp.next
        temp.next=newnode

    def display(self):
        if(self.head is None):
            print("Empty !")
        n=self.head
        while(self.head is not None):
            print(self.head.data,"-->",end=' ')
            self.head=self.head.next

root=linked_list()
root.AddLast(4)
root.AddLast(5)
# root.AddLast(6)
root.display()
