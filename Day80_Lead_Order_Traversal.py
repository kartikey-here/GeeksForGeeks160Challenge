#Given a root of a binary tree with n nodes, the task is to find its level order traversal. Level order traversal of a tree is breadth-first traversal for the tree.


"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def levelOrder(self, root):
        # Your code here
        levelOrder = []
        levelOrderTraversal = [root]
        while levelOrderTraversal:
            tmp = []
            itemNodes = []
            while levelOrderTraversal:
                item = levelOrderTraversal.pop(0)
                tmp.append(item.data)
                if item.left:
                    itemNodes.append(item.left)
                if item.right:
                    itemNodes.append(item.right)
            levelOrderTraversal = itemNodes
            levelOrder.append(tmp)
        return levelOrder
        # Your code here
        
