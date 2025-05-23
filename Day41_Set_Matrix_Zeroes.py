#You are given a 2D matrix mat[][] of size n×m. The task is to modify the matrix such that if mat[i][j] is 0, all the elements in the i-th row and j-th column are set to 0 and do it in constant space complexity.

#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        rowlength = len(mat)
        collength = len(mat[0])
        row =[0]*rowlength
        col = [0]*collength
        for i in range(rowlength):
            for j in range(collength):
                if mat[i][j]==0:
                    row[i] = 1
                    col[j] = 1
        for i in range(rowlength):
            for j in range(collength):
                if row[i]==1 or col[j]==1:
                    mat[i][j]=0
        return mat

        
