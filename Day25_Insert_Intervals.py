#Geek has an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith event and intervals is sorted in ascending order by starti. He wants to add a new interval newInterval= [newStart, newEnd] where newStart and newEnd represent the start and end of this interval.
#Help Geek to insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def insertInterval(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        fir=intervals[0][0]
        sec=intervals[0][1]
        x=[]
        for i in range(len(intervals)-1):
            if sec<intervals[i+1][0]:
                x.append([fir,sec])
                sec=intervals[i+1][1]
                fir=intervals[i+1][0]
            sec=sec if sec>intervals[i+1][1] else intervals[i+1][1]
        x.append([fir,sec if sec>intervals[-1][1] else intervals[-1][1]])
        return x
        # Code here


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertInterval(intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
        print("~")
# } Driver Code Ends
