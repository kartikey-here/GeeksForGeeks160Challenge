#Given a sorted array of distinct positive integers arr[], we need to find the kth positive number that is missing from arr[].  

#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        a=set([x+1 for x in range((arr[-1])+k+1)])
        b=list(a-set(arr))
        b.sort()
        return (b)[k-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
