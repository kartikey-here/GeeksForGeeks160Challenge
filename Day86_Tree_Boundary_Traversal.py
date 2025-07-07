#Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

#Left Boundary: This includes all the nodes on the path from the root to the leftmost leaf node. You must prefer the left child over the right child when traversing. Do not include leaf nodes in this section.

#Leaf Nodes: All leaf nodes, in left-to-right order, that are not part of the left or right boundary.

#Reverse Right Boundary: This includes all the nodes on the path from the rightmost leaf node to the root, traversed in reverse order. You must prefer the right child over the left child when traversing. Do not include the root in this section if it was already included in the left boundary.

#Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    
    def ctRight(self, root,solution):
        
        if root==None:
            return
        
        
    
        self.ctRight(root.right,solution)  
        if root.right==None:
            self.ctRight(root.left,solution)
            
        if root.left==None and root.right==None:
            pass
        else:
            
            solution.append(root.data)    
            
            
    def ctLeft(self,root,solution):
        if root==None:
            return
        
        if root.left==None and root.right==None:
            pass
        else:
            
            solution.append(root.data)
    
        self.ctLeft(root.left,solution)  
        if root.left==None:
            self.ctLeft(root.right,solution)
            
    def leaf(self,root,solution,flag):
        if root==None:
            return
        
        if root.left==None and root.right==None and flag==1:
            solution.append(root.data)
            
        self.leaf(root.left,solution,1)
        self.leaf(root.right,solution,1)
            
            
        
        
       
        
    
    def boundaryTraversal(self, root):
        
        
        solution1=[]
        solution2=[]
        solution3=[]
        self.ctRight(root.right,solution1)  
        self.ctLeft(root.left,solution2)
        self.leaf(root,solution3,0)
        solution=[]
        solution.append(root.data)
        solution=solution+solution2+solution3+solution1
        
        #print(solution)
        #print(st) 
        return solution
