#Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    
    n=len(arr)
    mi=ri=arr[0]
    ma=re=arr[0]
    for i in range(1,n):
        ma=max(ma+arr[i],arr[i])
        re=max(re,ma)
        mi=min(mi+arr[i],arr[i])
        ri=min(ri,mi)
    return re if ri==sum(arr) else max(re,sum(arr)-ri)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1
        print("~")

# } Driver Code Ends
