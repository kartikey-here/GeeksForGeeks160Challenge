#Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.



class Solution:
    def countTriplets(self, arr, target):
        # code here
        count = 0
        n = len(arr)
        if n<3:
            return 0
        count = 0
        for i in range(n-2):
            rem = target- arr[i]
            freq = {}
            for j in range(i+1, n):
                if rem - arr[j] in freq:
                    count += freq[rem-arr[j]]
                freq[arr[j]] = freq.get(arr[j], 0) + 1
        return count
        # code here
