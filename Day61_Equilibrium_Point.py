#Given an array of integers arr[], the task is to find the first equilibrium point in the array.
 
#The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 


# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        left_sum = arr[0]
        right_sum = sum(arr)
        for i in range(1, len(arr)):
            left_sum += arr[i - 1]
            right_sum -= arr[i]
            if left_sum == right_sum:
                return i
        return -1
        # code here

