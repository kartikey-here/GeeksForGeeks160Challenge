#A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum element in it. 

#User function Template for python3

class Solution:
    def findMin(self, arr):
        return min(arr)


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
