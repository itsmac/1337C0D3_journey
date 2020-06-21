'''
No: #1464. 
Title: Maximum Product of Two Elements in an Array
Level: Easy
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    ''' The below commented is using a built in python function sorted '''
        # nums = sorted(nums)
        # return (nums[-1]-1) * (nums[-2]-1)
        m,n = 0,0
        for i in nums:
            if i > m:
                n = m
                m = i
            else:
                n = max(n,i)
        return (m-1) * (n-1)
   
   
''' Getting the max and max-1 value is the solution 
taking the max value and storing 
if current value is greater than existing max
then replace the current with max and assign the old max to the second maximum variable
else check for the current val with the existing max-1 and replace it with the maxof cur vs existing'''        
