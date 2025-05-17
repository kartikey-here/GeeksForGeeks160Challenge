#You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.

class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        m,n=len(mat),len(mat[0])
        m_,n_=0,0
        i,j=0,0
        dir=1
        ans=[]
        while n_<n and m_<m:
            while n_<=j<n:
                ans.append(mat[i][j])
                j+=dir
            j-=dir
            i+=dir
            while m_<=i<m:
                ans.append(mat[i][j])
                i+=dir
            i-=dir
            j-=dir
            if dir==1:
                m_+=1
                n-=1
            else:
                m-=1
                n_+=1
            dir*=-1
        return ans
        # code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends
