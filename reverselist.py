import math
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
def KAltReverse(head,k):
    current=head
    next=None 
    prev=None 
    count=0
    while(current !=None and count<k):
        next=current.next
        current.next=prev
        prev=current
        current=next
        count=count+1
    if(head!=None):
        head.next=current
    count=0
    while(count<k-1 and current !=None):
        current=current.next
        count=count+1
    if (current !=None):
        current.next=kAltReverse(current.next.k)
    return prev
def push(head_ref,new_data):
    new_node= Node(new_data)
    new_node.next=head_ref
    head_ref=new_node
    return head_ref
    
def  prList(node):
    count=0
    while(node!=None):
        print(node.data,end=" ")
        node=node.next
        count=count+1
if __name__=='__main__':
    head=None 
n=int(input())
head=list(map(int,input().split()))
prList(head)

