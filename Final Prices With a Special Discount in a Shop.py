'''
No: 1475. 
Title: Final Prices With a Special Discount in a Shop
Level: Easy
'''

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l1 = [] #stores the index values
        for i,val in enumerate(prices):
            while l1 and prices[l1[-1]] >= val: # l1 must not null otherwise error at comparing
                prices[l1.pop()] -= val
            l1.append(i)
        return prices

'''
Use a stack for storing (keep track) index values
For every element in the list.
check for the last element stored in the stack (index of the last element).
if it is less than then pop it out and subtract the value with the current value
then whatsoever append the current iterator in stack to check
'''
        
