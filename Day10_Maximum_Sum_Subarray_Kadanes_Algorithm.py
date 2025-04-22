#Given an integer array arr[]. You need to find the maximum sum of a subarray.

class Solution:
    def maxSubArraySum(self, arr):
        ma=r=arr[0]
        for i in range(1,len(arr)):
            ma=max(ma+arr[i],arr[i])
            r=max(ma,r)
        return r


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
