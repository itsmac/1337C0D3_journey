'''
No: 1051. 
Title: Height Checker
'''

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != h[i]:
                count+=1
        return count
        
        
'''
First sort and then check the elements
if the both arra has diff element at same position then count+=1
[2,1,3,4,1]
[1,1,2,3,4]
ans: 4
'''
