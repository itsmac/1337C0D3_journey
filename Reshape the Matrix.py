'''
566. 
Reshape the Matrix
Easy
'''


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(nums),len(nums[0])
        if row*col == r*c:
            sub_arr = []
            res = []
            for i in nums:
                for j in i:
                    sub_arr.append(j)
            k = 0
            for i in range(r):
                sub_res = []
                for j in range(c):
                    sub_res.append(sub_arr[k])
                    k +=1
                res.append(sub_res)
            return res
        else:
            return nums
        
