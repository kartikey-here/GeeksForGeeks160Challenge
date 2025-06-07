#Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.
#Note: If no such array is possible then, return [-1].

#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        n = len(arr)
        start = 0
        current_sum = 0
    
        for end in range(n):
            current_sum += arr[end]
    
            while current_sum > target and start <= end:
                current_sum -= arr[start]
                start += 1
    
            if current_sum == target:
                # 1-based indexing
                return [start + 1, end + 1]
    
        return [-1]
        # code here
