#Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k

class Solution:
    def subarrayXor(self, arr, k):
        # code here
        freq={}
        xor=0
        c=0
        for i in arr:
            xor^=i
            if xor ==k:
                c+=1
            if xor^k in freq:
                c+=freq[xor^k]
            freq[xor]=freq.get(xor,0)+1
        return c
