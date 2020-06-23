'''
No: 1351. 
Title: Count Negative Numbers in a Sorted Matrix
Level: Easy
'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        #Brute force
        # for i in grid:
        #     for j in i:
        #         if j != abs(j):
        #             count+=1
        row, col = len(grid)-1,0
        while row >=0 and col < len(grid[0]):
            if grid[row][col] < 0:
                count += len(grid[0])-col
                row -=1
            else:
                col+=1
            
        return count

'''
Anyhow since this is a sorted matrix,
The elements will tend to form a staircase
so either start from top or bottom and traverse through
hence while iterating through rows, iterate column 
due to staircase pattern the negative values will be decreasing order in the pattern
'''
