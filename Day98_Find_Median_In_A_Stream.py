#Given a data stream arr[] where integers are read sequentially, the task is to determine the median of the elements encountered so far after each new integer is read.

#There are two cases for median on the basis of data set size.

#1. If the data set has an odd number then the middle one will be consider as median.
#2. If the data set has an even number then there is no distinct middle value and the median will be the arithmetic mean of the two middle values.

class Solution:
    def getMedian(self, arr):
        import heapq
        ret,up,dn=[],[],[]
        for ve in arr:
            ve=heapq.heappushpop(up,ve)
            ve=-heapq.heappushpop(dn,-ve)
            if len(up)==len(dn):
                ret.append(ve)
                heapq.heappush(up,ve)
            elif len(up)>len(dn):
                ret.append((up[0]+ve)/2)
                heapq.heappush(dn,-ve)
            else:
                ret.append((-dn[0]+ve)/2)
                heapq.heappush(up,ve)
        return ret
