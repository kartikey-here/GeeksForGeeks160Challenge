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
    
    def inOrder(self, root):
        if not root: return []   
        arr = []   
        arr += self.inOrder(root.left)
        arr.append(root.data)
        arr += self.inOrder(root.right)
        return arr
        
    def findTarget(self, root, target): 
        _lst = self.inOrder(root)
        _set = set(_lst)
        found = False
        for item in _lst:
            _set.remove(item)
            if target - item in _set:
                found = True
                break
        return found
