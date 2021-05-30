class node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LL:
    def __init__(self):
        self.head = None

    def printall(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end="")
                n = n.ref

    def insert_begin(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            new_node.ref = n
            self.head = new_node

    def insert_last(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def insert_inbet_before(self, data, x):
        new_node = node(data)
        if self.head is None:
            print("ll is empty")
        elif self.head.data == x:
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("X is not present")
            else:
                new_node.ref = n.ref
                n.ref = new_node

    def insert_after(self, data, x):
        new_node = node(data)
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head
            while n.ref is not None:
                if n.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("X is not present")
            else:
                new_node.ref = n.ref
                n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("ll is empty")
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("ll is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None


l1 = LL()
# l1.insert_begin(3)
# l1.insert_begin(3)
l1.insert_begin(3)
l1.insert_begin(4)
l1.insert_last(20)
l1.insert_inbet_before(40, 4)
# l1.insert_after(9,4)
# l1.delete_begin()
l1.delete_end()
l1.printall()
