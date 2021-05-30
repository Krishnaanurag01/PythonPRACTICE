class Node:
    def __init__(self, data):
        self.data = data
        self.Nref = None
        self.Pref = None


class Doubly_Linked_list:
    def __init__(self):
        self.head = None

    def Traverse_forward(self):
        print()
        if self.head is None:
            print("Linked_List is empty !")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=' ')
                n = n.Nref

    def Traverse_backward(self):
        print()
        if self.head is None:
            print("Linked_List is empty !")
        else:
            n = self.head
            while n.Nref is not None:
                n = n.Nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.Pref

    def Insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            new_node.Nref = n
            n.Pref = new_node
            self.head = new_node

    def Insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.Nref is not None:
                n = n.Nref
            n.Nref = new_node
            new_node.Pref = n

    def Insert_after(self, data, x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.Nref
            if n is None:
                print("X not found")
            else:
                new_node = Node(data)
                new_node.Nref = n.Nref
                new_node.Pref = n
                if n.Nref is not None:
                    n.Nref.Pref = new_node
                n.Nref = new_node

    def Insert_Before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.Nref
            if n is None:
                print("X not found")
            else:
                new_node = Node(data)
                new_node.Nref = n
                new_node.Pref = n.Pref
                if n.Pref is not None:
                    n.Pref.Nref = new_node
                else:
                    self.head = new_node
                n.Pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is already Empty!")
            return
        elif self.head.Nref is None:
            self.head = None
            print("The one and only element is deleted!")
        else:
            self.head = self.head.Nref
            self.head.Pref = None

    def delete_last(self):
        if self.head is None:
            print("Linked List is already Empty!")
            return
        elif self.head.Nref is None:
            self.head = None
            print("The one and only element is deleted!")
        else:
            n = self.head
            while n.Nref is not None:
                n = n.Nref
            print(f"{n.data} is deleted sucessfully!")
            n.Pref.Nref = None

    def delete_specific(self, x):
        if self.head is None:
            print("Linked List is already Empty!")
            return
        elif self.head.Nref is None:
            if x == self.head.data:
                self.head = None
                print("The one and only element is deleted!")
            else:
                print(f"{x} is not present")
            return
        if self.head.data == x:
            self.head = self.head.Nref
            self.head.Pref = None
        else:
            n = self.head
            while n.Nref is not None:
                if n.data == x:
                    n.Nref.Pref = n.Pref
                    n.Pref.Nref = n.Nref
                n = n.Nref
            if n.Nref is None:
                if n.data == x:
                    n.Pref.Nref = None
                else:
                    print(f"{x} not found !!!")


dl1 = Doubly_Linked_list()
# dl1.Insert_begin(2)
dl1.Insert_begin(4)
dl1.Insert_begin(5)
# dl1.Insert_after(40, 2)
# dl1.Insert_after(40, 5)
# dl1.Insert_Before(99,2)
# dl1.Insert_Before(96,32)
# dl1.delete_begin()
# dl1.delete_last()

dl1.delete_specific(5)
# dl1.delete_specific(4)


dl1.Traverse_forward()
# dl1.Traverse_backward()
