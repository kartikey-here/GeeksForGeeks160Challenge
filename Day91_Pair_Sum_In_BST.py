#Given a Binary Search Tree(BST) and a target. Check whether there's a pair of Nodes in the BST with value summing up to the target. 

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    
        
        
    def findTarget(self, root, target): 
        def ino(root,inorder):
            if root is None:
                return
            ino(root.left,inorder)
            inorder.append(root.data)
            ino(root.right,inorder)
        # your code here.
        inorder=[]
        ino(root, inorder)
        
        l,r=0,len(inorder)-1
        while l<r:
            cs=inorder[l]+inorder[r]
            
            if cs==target:
                return True
            if cs<target:
                l+=1
            else:
                r-=1
        return False
