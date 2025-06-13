#Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.


# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        dict1={0:-1}
        sm,ans=0,0
        for i in range(len(arr)):
            sm+=arr[i]
            if sm-k in dict1:
                ans=max(ans,i-dict1[sm-k])
            if sm not in dict1:
                dict1[sm]=i
        return ans
        # code here
    
