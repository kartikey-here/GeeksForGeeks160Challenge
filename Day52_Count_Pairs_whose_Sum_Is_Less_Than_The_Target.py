#Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly less than the target.



#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):  
        arr.sort()
        l,h,ans=0,len(arr)-1,0
        while l<h:
            val=arr[l]+arr[h]
            if val<target:
                ans+=(h-l)
                l+=1
            else:
                h-=1
        return ans
        #Your code here
