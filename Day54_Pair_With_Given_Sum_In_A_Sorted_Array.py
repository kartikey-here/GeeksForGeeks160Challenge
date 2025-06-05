#You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
#Note: pairs should have elements of distinct indexes. 

#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        s,e=0,len(arr)-1
        count=0
        while s<e:
            total=arr[s]+arr[e]
            if total>target:
                e-=1
            elif total<target:
                s+=1
            else:
                count+=1
                for i in range(e-1,s,-1):
                    if arr[s]+arr[i]==target:
                        count+=1
                for i in range(s+1,e):
                    if arr[e]+arr[i]==target:
                        count+=1
                s+=1;e-=1
        return count
        #Complete the function
