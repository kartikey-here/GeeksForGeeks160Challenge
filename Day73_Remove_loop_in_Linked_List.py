#Given the head of a linked list that may contain a loop.  A loop means that the last node of the linked list is connected back to a node in the same list. The task is to remove the loop from the linked list (if it exists).

#Custom Input format:

#A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.

#The generated output will be true if there is no loop in list and other nodes in the list remain unchanged, otherwise, false.


'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, heada):
        head=heada
        while(head.next!=None):
            if head.next.data=='c':
                head.next=None
                return head
            head.data='c'
            head=head.next
        return False
