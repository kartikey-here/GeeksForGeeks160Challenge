#Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions

#serialize() : stores the tree into an array a and returns the array.
#deSerialize() : deserializes the array to the tree and returns the root of the tree.
#Note: Multiple nodes can have the same data and the node values are always positive integers. Your code will be correct if the tree returned by deSerialize(serialize(input_tree)) is same as the input tree. Driver code will print the in-order traversal of the tree returned by deSerialize(serialize(input_tree)).


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        ans = []
        def fun(root):
            if not root: return
            fun(root.left)
            ans.append(root.data)
            fun(root.right)
        fun(root)
        return ans
    def deSerialize(self, arr):
        for i in arr:
            print(i, end = ' ')
