#Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. This path may or may not pass through the root. Your task is to find the diameter of the tree.

'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def height(self, root, diff):
        if not root: return -1
        l = 1 + self.height(root.left, diff)
        r = 1 + self.height(root.right, diff)
        diff[0] = max(diff[0], l + r)
        return max(l,r)
        
    def diameter(self, root):
        diff = [0]
        self.height(root, diff)
        return diff[0]
