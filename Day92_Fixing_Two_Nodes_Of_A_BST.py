#Given the root of a Binary search tree(BST), where exactly two nodes were swapped by mistake. Your task is to fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
#Note: It is guaranteed that the given input will form BST, except for 2 nodes that will be wrong. All changes must be reflected in the original Binary search tree(BST).



class Fix:
    def __init__(self):
        self.first=None
        self.second=None
        self.pred=Node(0)

class Solution:
    def solve(self,root,f):
        if root:
            self.solve(root.left,f)
            if root.data<f.pred.data:
                if not f.second:
                    f.second=f.pred
                f.first=root
            f.pred=root
            self.solve(root.right,f)
    
    def correctBST(self, root):
        f=Fix()
        self.solve(root,f)
        f.first.data,f.second.data=f.second.data,f.first.data
