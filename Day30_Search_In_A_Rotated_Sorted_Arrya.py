#Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key. Return -1 if the key is not found.

#User function Template for python3

class Solution:
    def search(self,arr,key):
        return arr.index(key) if key in arr else -1
        # Complete this function


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends
