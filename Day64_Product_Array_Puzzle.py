#Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. Return this resultant array, res[].
#Note: Each element is res[] lies inside the 32-bit integer range.

#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        n=len(arr)
        pre=1
        res=[1]*n
        for i in range(n):
            res[i] = pre
            pre=pre*arr[i]
        
        post=1
        for i in range(n-1,-1,-1):
            res[i]=res[i]*post
            post=post*arr[i]
        
        return res
