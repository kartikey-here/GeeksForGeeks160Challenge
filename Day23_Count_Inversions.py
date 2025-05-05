#Given an array of integers arr[]. Find the Inversion Count in the array.
#Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.
#Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
#If an array is sorted in the reverse order then the inversion count is the maximum. 

class Solution:
    def cam(self,arr,l,m,r):
        n1=m-l+1
        n2=r-m
        le=arr[l:m+1]
        ri=arr[m+1:r+1]
        res=i=j=0
        k=l
        while i<n1 and j<n2:
            if le[i]<=ri[j]:
                arr[k]=le[i]
                i+=1
            else:
                arr[k]=ri[j]
                j+=1
                res+=(n1-i)
            k+=1
        while i<n1:
            arr[k]=le[i]
            i+=1
            k+=1
        while j<n2:
            arr[k]=ri[j]
            j+=1
            k+=1
        return res
    def ci(self,arr,l,r):
        res=0
        if l<r:
            m=(r+l)//2
            res+=self.ci(arr,l,m)
            res+=self.ci(arr,m+1,r)
            res+=self.cam(arr,l,m,r)
        return res
    def inversionCount(self, arr):
        return self.ci(arr,0,len(arr)-1)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends
