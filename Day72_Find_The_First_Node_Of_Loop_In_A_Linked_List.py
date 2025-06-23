#Given a head of the singly linked list. If a loop is present in the list then return the first node of the loop else return NULL.

#Custom Input format:
#A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.

#User function Template for python3

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
class Solution:
    #Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):
        
        slow = head
        fast = head
        
        while fast and fast.next:
        
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
