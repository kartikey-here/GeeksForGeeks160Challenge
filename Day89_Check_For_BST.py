#Given the root of a binary tree. Check whether it is a BST or not.
#Note: We are considering that BSTs can not contain duplicate Nodes.
#A BST is defined as follows:

#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def sol(self, root, min_val, max_val):
            if root is None:
                return True
            if root.data >= max_val or root.data <= min_val:
                return False
            return self.sol(root.left, min_val, root.data) and self.sol(root.right, root.data, max_val)

    def isBST(self, root): 
            min_val = -sys.maxsize - 1  
            max_val = sys.maxsize       
            return self.sol(root, min_val, max_val)
