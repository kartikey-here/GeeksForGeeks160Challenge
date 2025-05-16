#You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:
#
#Each student receives atleast one book.
#Each student is assigned a contiguous sequence of books.
#No book is assigned to more than one student.
#The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

#Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

class Solution:
    
    #Function to find minimum number of pages.
    def cntStudents(self,arr,pages):
        students=1
        pagesStudent=0
        n=len(arr)
        for i in range(n):
            if pagesStudent+arr[i]<=pages:
                pagesStudent+=arr[i]
            else:
                students+=1
                pagesStudent=arr[i]
        return students

    def findPages(self, arr, k):
        if len(arr)<k:
            return -1
        l,h=max(arr),sum(arr)
        while l<=h:
            mid=(l+h)//2
            students=self.cntStudents(arr,mid)
            if students>k:
                l=mid+1
            else:
                h=mid-1
        return l


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
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
