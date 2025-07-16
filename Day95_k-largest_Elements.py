#Given an array arr[] of positive integers and an integer k, Your task is to return k largest elements in decreasing order. 


class Solution:
    def kLargest(self, arr, k):
        n= len(arr)
        arr.sort(reverse = True)
        return arr[:k]
        # Your code here
