#You are given a two-dimensional mat[][] of size n*m containing English alphabets and a string word. Check if the word exists on the mat. The word can be constructed by using letters from adjacent cells, either horizontally or vertically. The same cell cannot be used more than once.

class Solution:
    
    d=[(0,1),(0,-1),(1,0),(-1,0)]
    
    def dfs(self,mat,word,visited,i,j,ind):
        row,col=len(mat),len(mat[0])
        if mat[i][j]!=word[ind]:
            return False
        if ind==len(word)-1:
            return True
        visited[i][j]=True
        for dx,dy in self.d:
            x,y=i+dx,j+dy
            if 0<=x<row and 0<=y<col and visited[x][y]==False:
                if self.dfs(mat,word,visited,x,y,ind+1):
                    return True
        visited[i][j]=False
        return False
    
    def isWordExist(self, mat, word):
        row,col=len(mat),len(mat[0])
        visited=[[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if self.dfs(mat,word,visited,i,j,0):
                    return True
        return False
