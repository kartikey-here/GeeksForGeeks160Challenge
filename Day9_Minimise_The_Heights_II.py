#Given an array arr[] denoting heights of N towers and a positive integer K.
#For each tower, you must perform exactly one of the following operations exactly once.
#Increase the height of the tower by K
#Decrease the height of the tower by K
#Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.
#You can find a slight modification of the problem here.
#Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        l=len(arr)
        arr.sort()
        dif=arr[l-1]-arr[0]
        for i in range(l):
            if arr[i]<k:
                continue
            mi=min(arr[0]+k,arr[i]-k)
            ma=max(arr[i-1]+k,arr[l-1]-k)
            dif=min(dif,ma-mi)
        return dif
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends
