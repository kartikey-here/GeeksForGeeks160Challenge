#You are given the head of a singly linked list. Your task is to determine if the linked list contains a loop. A loop exists in a linked list if the next pointer of the last node points to any other node in the list (including itself), rather than being null.

#Custom Input format:
#A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.

#User function Template for python3
'''
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    
'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        while(head!=None):
            if head.data=='c':
                return True
            head.data='c'
            head=head.next
        return False
        


    
