'''
169. 
Majority Element
Easy
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        res = 0
        k = 0
        for key,val in d.items():
            if res < val:
                k = key
                res = val
        return k
