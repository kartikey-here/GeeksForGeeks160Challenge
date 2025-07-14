#Given a Binary Search Tree (with all values unique) and two nodes n1 and n2 (n1 != n2). You may assume that both nodes exist in the tree. Find the Lowest Common Ancestor (LCA) of the given two nodes in the BST.

#LCA between two nodes n1 and n2 is defined as the lowest node that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def findLCA(self, root,l,h):
        if not root:
            return None
        if root.data >= l and root.data <= h:
            return root
        l_s = self.findLCA(root.left,l,h)
        r_s = self.findLCA(root.right,l,h)
        
        if l_s is not None:
            return l_s
        else:
            return r_s
        
    def LCA(self, root, n1, n2):
        # your code here
        l = min(n1.data,n2.data)
        h = max(n1.data,n2.data)
        
        lca = self.findLCA(root,l,h)
        
        return lca
        # your code here
        
    
