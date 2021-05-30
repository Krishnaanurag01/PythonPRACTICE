class bst:
    def __init__(self,key):
        self.key=key
        self.Lchild=None
        self.Rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if data<self.key:
            if self.Lchild:
                self.Lchild.insert(data)
            else:
                self.Lchild=bst(data)
        else:
            if self.Rchild:
                self.Rchild.insert(data)
            else:
                self.Rchild=bst(data)

    def search(self,data):
        if self.key==data:
            print(f"Node {self.key} is present  !")
        elif self.key>data:
            if self.Lchild:
                self.Lchild.search(data)
            else:
                print("Node not present")
        else:
            if self.Rchild:
                self.Rchild.search(data)
            else:
                print("Node not present")
    
    def Traversal_Pre_Order(self):
        print(self.key,end=' ')
        if self.Lchild:
            self.Lchild.Traversal_Pre_Order()
        if self.Rchild:
            self.Rchild.Traversal_Pre_Order()

    def Traversal_In_Order(self):
        if self.Lchild:
            self.Lchild.Traversal_In_Order()
        print(self.key,end=' ')
        if self.Rchild:
            self.Rchild.Traversal_In_Order()

    def Traversal_Post_Order(self):
        if self.Lchild:
            self.Lchild.Traversal_Post_Order()
        if self.Rchild:
            self.Rchild.Traversal_Post_Order()
        print(self.key,end=' ')

    def delete(self,data,curr):
        if self.key is None:
            print("Tree is empty !")
            return
        if data<self.key:
            if self.Lchild:
                self.Lchild=self.Lchild.delete(data,curr)
            else:
                print("Data Not Present !!")
        elif data>self.key:
            if self.Rchild:
                self.Rchild=self.Rchild.delete(data,curr)
            else:
                print("Data Not Present !!")
        else:
            if self.Lchild is None:
                temp=self.Rchild
                if data==curr:
                    self.key=temp.key
                    self.Lchild=temp.Lchild
                    self.Rchild=temp.Rchild
                    temp=None
                    return
                self=None
                return temp
            if self.Rchild is None:
                temp=self.Lchild
                if data==curr:
                    self.key=temp.key
                    self.Lchild=temp.Lchild
                    self.Rchild=temp.Rchild
                    temp=None
                    return
                self=None
                return temp
            node=self.Rchild
            while node.Lchild:
                node=node.Lchild
            self.key=node.key
            self.Rchild=self.Rchild.delete(node.key)
        return self

    def smallest_key(self):
        # if not self.Lchild :
        #     print(f"{self.key} is smallest")
        # else:
        #     if self.Lchild:
        #         self.Lchild.smallest_key()
        current=self
        while current.Lchild:
            current=current.Lchild
        print("Smallest key is,",current.key)
    
    def largest_key(self):
        current=self
        while current.Rchild:
            current=current.Rchild
        print("Largest key is,",current.key)
    



def count(node):
    if node is None:
        return 0
    return 1+count(node.Lchild)+count(node.Rchild)



root=bst(10)
l=[11,12,13]
for i in l:
    root.insert(i)

# if count(root)>1:
#     root.delete(int(input()),root.key)
# else:
#     print("Can't delete the node !!")

# print(root.Traversal_Pre_Order())
print(root.smallest_key())
print(root.largest_key())