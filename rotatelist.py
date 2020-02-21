
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printlist(self):
        temp=self.head
        while(temp):
            temp=temp.next
    def rotate(self,k):
        if k==0:
            return
        current=self.head
        count=1
        while(count<k and current is not None):
            current=current.next
            count+=1
        if current is None:
            return
        kthNode=current
        while(current.next is not None):
            current=current.next
        current.next=self.head
        self.head=kthNode.next
        kthNode.next=None
llist=LinkedList()
n=int(input())
llist=input().split()
print(*llist)
m=int(input())
llist.rotate(m)
print(*llist)

