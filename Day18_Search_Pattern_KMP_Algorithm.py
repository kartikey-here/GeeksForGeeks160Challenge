#Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices. 
#Note: Return an empty list in case of no occurrences of pattern.


#User function Template for python3

class Solution:
    def search(self, pat, txt):
        a=[]
        p=len(pat)
        for i in range(len(txt)-p+1):
            if txt[i:i+p]==pat:
                a.append(i)
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends
