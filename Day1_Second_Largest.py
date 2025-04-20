#Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
#Note: The second largest element should not be equal to the largest element.

class Solution:
    def getSecondLargest(self, arr):
        arr.sort()
        l=arr[len(arr)-1]
        a=-1
        while(len(arr)>1):
            arr.pop()
            if(arr[len(arr)-1]!=l):
                a=arr[len(arr)-1]
                break
        return l if l==a else a
      
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
