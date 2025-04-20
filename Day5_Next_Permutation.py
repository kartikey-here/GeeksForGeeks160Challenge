#Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 
#Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        n=len(arr)
        i=n-2
        while i>=0 and arr[i]>=arr[i+1]:
            i-=1
        if i>=0:
            j=n-1
            while arr[j]<=arr[i]:
                j-=1
            arr[j],arr[i]=arr[i],arr[j]
        arr[i+1:]=reversed(arr[i+1:])
        return arr
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends
