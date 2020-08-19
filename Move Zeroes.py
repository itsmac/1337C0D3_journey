'''
283. 
Move Zeroes
Easy
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastfound = 0
        for current in range(len(nums)):
            if nums[current] != 0 :
                nums[lastfound],nums[current] = nums[current],nums[lastfound]
                lastfound+=1

        
