#Given an array arr[] and an integer target. You have to find numbers of pairs in array arr[] which sums up to given target.


#User function Template for python3

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        
        d=dict()
        count=0
        
        for i in arr:
            if (target-i) in d:
                count+=d[target-i]
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        return count
        
        #Your code here
