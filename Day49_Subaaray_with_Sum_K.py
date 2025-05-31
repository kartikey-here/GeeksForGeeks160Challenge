#Given an unsorted array of integers, find the number of subarrays having sum exactly equal to a given number k.

#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        n=len(arr)
        d={0:1}
        preSum=0
        count=0
        
        for i in range(n):
            preSum+=arr[i]
            if (preSum-k) in d:
                count+=d[preSum-k]
            
            if preSum in d:
                d[preSum]+=1
            else:
                d[preSum]=1

        return count
        # code here
