#Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.


 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        arr.sort()
        res=1
        cnt=1
        for i in range(1,len(arr)):
            if(arr[i]==arr[i-1]):
                continue
            if(arr[i]==arr[i-1]+1):
                cnt+=1
            else:
                cnt=1
            res=max(res,cnt)
        return res
        #code here
