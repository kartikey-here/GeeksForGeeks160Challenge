#Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def minRemoval(self, arr):
        c=0
        arr.sort()
        sec=arr[0][1]
        for i in range(1,len(arr)):
            if arr[i][0]<sec:
                c+=1
                sec=min(arr[i][1],sec)
            else:
                sec=arr[i][1]
        return c
        # Code here


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends
