class Node:
    def __init__(self,data):
        self.data= data
        self.link=None

class Linkedlist:
    def __init__(self):
        self.head =None

    def Traverse_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"---->",end=" ")
                n= n.link

    def insertAtBeginning(self,data):
        new_node= Node(data)
        new_node.link=self.head
        self.head=new_node

    def insertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.link is not None:
                n=n.link
            n.link=new_node

    def insertAtAfterIndex(self,data,index):
        n= self.head
        while n is not None:
            if n.data==index:
                break
            else:
                n=n.link
        if n is None:
            print("Node is not present in the linked list")
        else:
            new_node=Node(data)
            new_node.link=n.link
            n.link=new_node

    def insertAtBeforeIndex(self,data,index):
        if self.head is None:
            print("LinkedList is Empty")
            return
        if self.head.data==index:
            new_node= Node(data)
            new_node.link=self.head
            self.head=new_node
            return
        n=self.head
        while n is not None:
            if n.link.data==index:
                break
            else:
                n=n.link
        if n is None:
            print("Node is not present in the linked list")
        else:
            new_node=Node(data)
            new_node.link=n.link
            n.link=new_node

    def Delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head=self.head.link

    def Delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n= self.head
            while n.link.link is not None:
                n=n.link            
            n.link=None
    
    def Delete_At_Given_Value(self,Index):
        if self.head is None:
            print("Linked list is Empty")
            return
        if Index==self.head.data:
            self.head=self.head.link
        n= self.head
        while n.link is not None:
            if Index==n.link.data:
                break
            n=n.link
        if n.link is None:
            print("Node is not present in the Linked list")
        else:
            n.link=n.link.link





Linkedlist1 = Linkedlist()
Linkedlist1.insertAtBeginning(55)
Linkedlist1.insertAtEnd(100)
Linkedlist1.insertAtBeginning(78)
Linkedlist1.insertAtBeginning(95)
Linkedlist1.insertAtEnd(200)
Linkedlist1.insertAtBeginning(25)
Linkedlist1.insertAtAfterIndex(6372,78)
Linkedlist1.insertAtEnd(300)
Linkedlist1.insertAtAfterIndex(5000,200)
Linkedlist1.insertAtBeforeIndex(378901,5000)
Linkedlist1.Delete_end()
Linkedlist1.Delete_At_Given_Value(100)
Linkedlist1.Delete_At_Given_Value(78)
Linkedlist1.Delete_At_Given_Value(5000)
Linkedlist1.Traverse_LL()
    