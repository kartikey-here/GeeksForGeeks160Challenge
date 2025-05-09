#Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

class Solution:
    def mergeArrays(self, a, b):
        n=len(a)
        m=len(b)
        gap=(n+m+1)//2
        while gap>0:
            i=0
            j=gap
            while j<n+m:
                if j<n and a[i]>a[j]:
                    a[i],a[j]=a[j],a[i]
                elif i<n and j>=n and a[i]>b[j-n]:
                    a[i],b[j-n]=b[j-n],a[i]
                elif i>=n and b[i-n]>b[j-n]:
                    b[i-n],b[j-n]=b[j-n],b[i-n]
                i+=1
                j+=1
            if gap==1:
                break
            gap=(gap+1)//2
        
        # code here


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

        print("~")

# } Driver Code Ends
