#Given a binary tree, find its height.

#The height of a tree is defined as the number of edges on the longest path from the root to a leaf node. A leaf node is a node that does not have any children.

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if not root:
            return -1
        return max(1 + self.height(root.left), 1 + self.height(root.right)) 
        # code here
