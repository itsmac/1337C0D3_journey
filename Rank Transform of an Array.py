'''
1331. 
Rank Transform of an Array
Easy
'''

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        res = []
        index = 1
        for i in sorted(arr):
            if i not in d:
                d[i] = index
                index+=1
        for i in arr:
            res.append(d[i])
        return res
            
