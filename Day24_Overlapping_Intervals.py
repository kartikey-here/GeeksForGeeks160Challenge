#Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.

class Solution:
	def mergeOverlap(self, arr):
	    arr.sort()
	    fir=arr[0][0]
	    sec=arr[0][1]
	    x=[]
	    for i in range(len(arr)-1):
	        if sec<arr[i+1][0]:
	            x.append([fir,sec])
	            sec=arr[i+1][1]
	            fir=arr[i+1][0]
	        sec=sec if sec>arr[i+1][1] else arr[i+1][1]
	    x.append([fir,sec if sec>arr[-1][1] else arr[-1][1]])
		return x


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends
