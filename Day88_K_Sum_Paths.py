#Given a binary tree and an integer k, determine the number of downward-only paths where the sum of the node values in the path equals k. A path can start and end at any node within the tree but must always move downward (from parent to child).

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def solve(self,root,k,currSum,preSum):
        if root:
            currSum[0]+=root.data
            ans=preSum.get(currSum[0]-k,0)
            preSum[currSum[0]]=preSum.get(currSum[0],0)+1
            ans+=self.solve(root.left,k,currSum,preSum)
            ans+=self.solve(root.right,k,currSum,preSum)
            preSum[currSum[0]]-=1
            currSum[0]-=root.data
            return ans
        return 0

    def sumK(self,root,k):
        currSum=[0]
        preSum={0:1}
        return self.solve(root,k,currSum,preSum)
