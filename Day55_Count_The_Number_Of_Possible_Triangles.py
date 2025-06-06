#Given an integer array arr[]. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle. 

#A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.

#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):

        arr.sort()
        n,ans=len(arr),0
        for i in range(n-1,1,-1):
            l,h=0,i-1
            while l<h:
                if arr[l]+arr[h]>arr[i]:
                    ans+=(h-l)
                    h-=1
                else:
                    l+=1
        return ans        # code here
