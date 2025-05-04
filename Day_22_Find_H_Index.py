#Given an integer array citations[], where citations[i] is the number of citations a researcher received for the ith paper. The task is to find the H-index.
#H-Index is the largest value such that the researcher has at least H papers that have been cited at least H times.

#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        citations.sort()
        n=len(citations)
        ma=max(citations)
        x=[0]*(ma+1)
        for i in citations:
            x[i]+=1
        a=[citations.count(ma)]
        for i in range(ma):
            a.append(a[i]+x[ma-1-i])
        x=0
        for i in range(len(a)):
            if ma-i<=a[i]:
                return ma-i
        return x


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends
