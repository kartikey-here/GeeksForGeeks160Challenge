#Given an array of points where each point is represented as points[i] = [xi, yi] on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
#The distance between two points on the X-Y plane is the Euclidean distance, defined as: 
#sqrt( (x2 - x1)2 + (y2 - y1)2 )
#Note: You can return the k closest points in any order, driver code will sort them before printing.

class Points:

    def __init__(self,x,y):

        self.x=x

        self.y=y

    def __gt__(self,oth):

        return self.x**2+self.y**2 < oth.x**2+oth.y**2

 

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        import heapq

        pq = []

        for [x,y] in points:

            if len(pq) < k:

                heapq.heappush(pq,Points(x,y))

            else:

                heapq.heappushpop(pq,Points(x,y))

        res = []

        for p in pq:

            res.append([p.x,p.y])

        return res
