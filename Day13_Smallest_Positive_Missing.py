#You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.
#Note: Positive number starts from 1. The array can have negative integers too.

#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        arr=set(arr)
        ma=max(arr)
        for i in range(1,ma):
            if i not in arr:
                return i
        return ma+1 if ma+1>0 else 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
