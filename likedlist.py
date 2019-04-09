class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
        

class LinkedList(object):
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.val)
            temp=temp.next
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def insetAfter(self,prevNode,new_data):
        if prevNode is None:
            print("there is no previous node")
            return
        new_node=Node(new_data)
        new_node.next=prevNode.next
        prevNode.next=new_node
    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def deleteNode(self,key):
        temp=self.head
        if(temp is not None):
            if(temp.val==key):
                self.head=temp.next
                temp=None
                return
        while(temp is not None):
            if(temp.val==key):
                break
            prev=temp
            temp=temp.next
        if(temp==None):
            return
        prev.next=temp.next
        temp=None
    def deletePosition(self,position):
        if self.head is None:
            return
        temp=self.head
        if(position==0):
            self.head=temp.next
            temp=None
            return
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        some=temp.next.next
        temp.next=None
        temp.next=some
            

if __name__=='__main__':
     llist=LinkedList()
     llist.head=Node(1)
     second=Node(2)
     third=Node(3)
     llist.head.next=second
     second.next=third
     llist.push(0)
     llist.insetAfter(second,2.5)
     llist.append(4)
     llist.deleteNode(0)
     llist.deletePosition(0)
     llist.printList()