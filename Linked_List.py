class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_list:
    def __init__(self):
        self.head=None

    def print_all(self):
        if self.head is None:
            print("Linked_List is Empty !!")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=' ')
                n=n.ref

    def insert_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def insert_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print(f"{x} is not in Linked list !") 
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def insert_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
        if x==self.head.data:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print(f"{x} not found !!")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty !")
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty so you can't delete from it !")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def delete_specific_element(self,x):
        if self.head is None:
            print("Linked List is empty !")
            return
        elif self.head.data==x :
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                n.ref=n.ref.ref
                return
            n=n.ref
        if n.ref is None:
            print("Choose correct element !")

        



ll=Linked_list()
ll.insert_begin(20)
ll.insert_begin(30)
ll.insert_begin(40)
# ll.insert_begin(50)
# ll.delete_end()
# ll.delete_begin()
# ll.insert_after(input(),int(input()))
# ll.insert_before(input(),int(input()))
ll.delete_specific_element(70)
ll.print_all()



