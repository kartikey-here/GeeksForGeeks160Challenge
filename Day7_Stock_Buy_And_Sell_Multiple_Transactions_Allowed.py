#The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.
#Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.

from typing import List

class Solution:
    def maximumProfit(self, prices) -> int:
        r=len(prices)
        sum=0
        # code here
        #print(prices)
        j=prices[0]
        #print('j    price[i],   price[i+1]  sum')
        for i in range(r-1):
            #print(j,prices[i],prices[i+1],sum)
            if(prices[i]==j and prices[i]>prices[i+1]):
                j=prices[i+1]
            elif(prices[i+1]<=prices[i]):
                sum+=prices[i]-j
                j=prices[i+1]
        return sum+prices[r-1]-j

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)
        print("~")

# } Driver Code Ends
