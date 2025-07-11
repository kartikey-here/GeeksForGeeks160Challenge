#Given a BST and an integer k, the task is to find the kth smallest element in the BST. If there is no kth smallest element present then return -1.

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        def inOrder(root):
            if not root: return []
            arr = []
            arr += inOrder(root.left)
            arr.append(root.data)
            arr += inOrder(root.right)
            return arr
        arr = inOrder(root)
        k = k - 1
        return arr[k] if k < len(arr) else -1
        #code here.
