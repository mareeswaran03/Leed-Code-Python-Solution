class Node:
    def __init__(self,data):
        self.data=data
        self.nlink=None
        self.plink=None


class doubly_linked_list:
    def __init__(self):
        self.head=None
    
    def Traverse_DLL(self):
        print("Forward Traversing")
        if self.head is None:
            print("Doubly Linked List is empty")
        n=self.head
        while n is not None:
            print(n.data,"--->",end=" ")
            n=n.nlink

    def Traverse_DLL_reverse(self):
        print()
        print("BackWard Traversing")
        n=self.head
        while n.nlink is not None:
            n=n.nlink
        while n is not None:
            print(n.data,"--->",end=" ")
            n=n.plink

    def add_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Doubly Linked List is Not empty")
    
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nlink=self.head
            self.head.plink=new_node
            self.head=new_node
    
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nlink is not None:
                n=n.nlink
            new_node.plink=n
            n.nlink=new_node

    def add_after(self,data,index):
        if self.head is None:
            print("Linked List is Empty, Can't add data to the Doubly LL")
        else:
            n=self.head
            while n is not None:
                if index==n.data:
                    break
                n=n.nlink
            if n is None:
                print("Given Node not present in the Doubly LL")
            else:
                new_node=Node(data)
                new_node.nlink=n.nlink
                new_node.plink=n
                if n.nlink is not None:
                    n.nlink.plink=new_node
                n.nlink=new_node
            
    def add_before(self,data,index):
        if self.head is None:
            print("Linked List is Empty, Can't add data to the Doubly LL")
        else:
            n=self.head
            while n is not None:
                if index==n.data:
                    break
                n=n.nlink
            if n is None:
                print("Given Node not present in the Doubly LL")
            else:
                new_node=Node(data)
                new_node.nlink=n
                new_node.plink=n.plink
                if n.plink is not None:
                    n.plink.nlink=new_node
                else:
                    self.head=new_node
                n.plink=new_node


DLL=doubly_linked_list()
DLL.add_empty(10)
DLL.add_begin(20)
DLL.add_end(1002)
DLL.add_after(150,1002)
DLL.add_before(300,20)
DLL.Traverse_DLL()
DLL.Traverse_DLL_reverse()

    