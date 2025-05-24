#Given an array arr[] of positive integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.


#User function Template for python3
class Solution:
    def twoSum(self, arr, target):
        seen = set()  
        for i in range(len(arr)):
            diff = target - arr[i]
            if diff in seen:
                return True  
            seen.add(arr[i])  
        return False  
        # code here
