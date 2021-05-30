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

    def delete(self,data):
        if self.key is None:
            print("Tree is empty !")
            return
        if data<self.key:
            if self.Lchild:
                self.Lchild=self.Lchild.delete(data)
            else:
                print("Data Not Present !!")
        elif data>self.key:
            if self.Rchild:
                self.Rchild=self.Rchild.delete(data)
            else:
                print("Data Not Present !!")
        else:
            if self.Lchild is None:
                temp=self.Rchild
                self=None
                return temp
            if self.Rchild is None:
                temp=self.Lchild
                self=None
                return temp
            node=self.Rchild
            while node.Lchild:
                node=node.Lchild
            self.key=node.key
            self.Rchild=self.Rchild.delete(node.key)
        return self



root=bst(10)
# l=[4,5,6,7,8,2,1]
# for i in l:
#     root.insert(i)


print(root.Traversal_Pre_Order())

root.delete(10)

print(root.Traversal_Pre_Order())