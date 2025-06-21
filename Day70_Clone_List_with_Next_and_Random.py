#You are given a special linked list with n nodes where each node has two pointers a next pointer that points to the next node of the singly linked list, and a random pointer that points to the random node of the linked list.

#Construct a copy of this linked list. The copy should consist of the same number of new nodes, where each new node has the value corresponding to its original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list, such that it also represent the same list state. None of the pointers in the new list should point to nodes in the original list.

#Return the head of the copied linked list.

#NOTE : Original linked list should remain unchanged.

# Link list Node
# class Node:

#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.random = None
        
class Solution:
    def cloneLinkedList(self, head):
        # code here
        
        dummy = w = Node(0)
        m = {}
        
        while head:
            if head not in m:
                m[head] = Node(head.data)
            cur = m[head]
            if head.random and head.random not in m:
                m[head.random] = Node(head.random.data)
            cur.random = m.get(head.random, None)
            w.next = cur
            
            w = w.next
            head = head.next
        return dummy.next
        # code here
