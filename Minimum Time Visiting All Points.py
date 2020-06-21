'''
No : #1266. 
Title : Minimum Time Visiting All Points
Level: Easy
'''


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        i = 0
        res = 0
        while(i<len(points)-1):
            temp = 0
            a,b = points[i]
            c,d = points[i+1]
            temp = max(abs(c-a),abs(d-b))
            res += temp
            i+=1
        return res
        
        
'''
Notes:
Taking the max value of the the diff between the coordinates
gets the minimum time for moving from a point to next point in a graph
Hence summing up will return the result
'''        
