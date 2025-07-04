#Given a binary tree, convert the binary tree to its Mirror tree.

#Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged. 

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        if not root:
            return
        root.left,root.right = root.right,root.left
        self.mirror(root.left)
        self.mirror(root.right)
        # Code here
