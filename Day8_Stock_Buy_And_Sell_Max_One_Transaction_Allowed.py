#Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.
#Note: Stock must be bought before being sold.

class Solution:
    def maximumProfit(self, prices):
        l=len(prices)
        a=list(prices)
        a.sort()
        if prices==a:
            #print('cond1',a,prices)
            return a[l-1]-a[0]
        a.sort(reverse=True)
        if prices==(a):
            #print('cond2')
            return 0
        x=0
        s=prices[0]
        for i in range(l):
            if s>prices[i]:
                s=prices[i]
            else:
                x=max(x,prices[i]-s)
        return (x)
        # code here

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends
