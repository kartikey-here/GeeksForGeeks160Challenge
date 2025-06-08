#Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

class Solution:
    def countDistinct(self, arr, k):
        output = []
        for w_id in range(len(arr)-k+1):
            output.append(len(set(arr[w_id:(w_id+k)])))
        return output
        # Code here
