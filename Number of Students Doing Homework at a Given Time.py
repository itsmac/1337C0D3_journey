'''
No: #1450. 
Title: Number of Students Doing Homework at a Given Time
Level: Easy
'''

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        i = 0
        res = 0
        while i < len(startTime) :
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                res +=1
            i+=1
        return res
      
'''
given query time must be between start and end time, s<= querytime <= e
'''
