#Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
#Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        ans=[0,float("inf")]
        l,h=0,len(arr)-1
        while l<h:
            val=arr[l]+arr[h]
            if abs(sum(ans)-target)>abs(val-target):
                ans[0],ans[1]=arr[l],arr[h]
            if target<val:
                h-=1
            else:
                l+=1
        return ans if len(arr)!=1 else []
        # code here
