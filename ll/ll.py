class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def linkprint(head):
        while head is not None:
            print(head.data,"->",end=" ")
            head = head.next    
def takeinput():
    inputlist = [int(a) for a in input().split()]
    head = None
    tail = None
    for currdata in inputlist:
        newnode = Node(currdata)
        if head is None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = newnode
            # curr = head
            # while curr.next is not None:
            #     curr = curr.next
            # curr.next = newnode
    return head
def insetat():
    
            

head1 = takeinput()
linkprint(head1) 



