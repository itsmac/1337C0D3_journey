'''
No: 1380. 
Title: Lucky Numbers in a Matrix
'''


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        l1,l2 = [],[]
        res = []
        for i in matrix:
            l1.append(min(i))
        for i in range(len(matrix[0])):
            max_val = 0
            for j in range(len(matrix)):
                if matrix[j][i] > max_val:
                    max_val = matrix[j][i]
            l2.append(max_val)
        for i in l1:
            if i in l2:
                res.append(i)
        return res
        
'''
find max element in row
find min element in col
then find the recurrin elements in both the list
'''
