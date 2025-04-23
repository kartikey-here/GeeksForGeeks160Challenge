#Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].
#Note: It is guaranteed that the output fits in a 32-bit integer.

#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
	    ma=-1221123
	    lr=rl=1
	    l=len(arr)
	    for i in range(l):
	        lr=1 if lr==0 else lr
	        rl=1 if rl==0 else rl
	        lr=lr*arr[i]
	        rl=rl*arr[l-1-i]
	        ma=max(lr,rl,ma)
	    return ma
	        
	        
        #{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
