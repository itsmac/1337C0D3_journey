'''
No: 561. 
Title: Array Partition I
'''


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        val = 0
        while(i <= len(nums)-2):
            val += nums[i]
            i +=2
        return val
        
            
'''
Sort the array. and sum of the first elements will give the val (since the min(pair))
'''
