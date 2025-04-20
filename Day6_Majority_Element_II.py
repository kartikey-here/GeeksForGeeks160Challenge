#You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 
#Note: The answer should be returned in an increasing format.

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        l=len(arr)
        a=[]
        aset=set(arr)
        for i in aset:
            if arr.count(i)>l//3:
                a.append(i)
        a.sort()
        return a
        #Your Code goes here.


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
