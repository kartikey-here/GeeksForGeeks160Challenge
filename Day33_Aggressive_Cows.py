#You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. Your task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.


class Solution:
    def canPlaceCowsatMidDist(self,arr,mid,c):
        cowCount=1
        prevCowPos=arr[0]
        for i in range(1,len(arr)):
            if arr[i]-prevCowPos>=mid:
                cowCount+=1
                prevCowPos=arr[i]
        if cowCount<c:
            return False
        return True
    
    
    
    def solve(self,arr,n,c):
        s=0
        e=arr[-1]-arr[0]
        ans=-1
        while s<=e:
            mid=s+(e-s)//2
            if self.canPlaceCowsatMidDist(arr,mid,c):
                ans=mid
                s=mid+1
            else:
                e=mid-1
        return ans
    def aggressiveCows(self, stalls, k):
        # your code here
        stalls.sort()
        return self.solve(stalls,len(stalls),k)
        # your code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends
