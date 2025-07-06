#Given a Binary Tree, your task is to return its In-Order Traversal.

#An inorder traversal first visits the left child (including its entire subtree), then visits the node, and finally visits the right child (including its entire subtree).

#Follow Up: Try solving this with O(1) auxiliary space.

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        # code here
        if root is None:
            return []
        else:
            return self.inOrder(root.left) + [root.data] + self.inOrder(root.right) 
        # code here
