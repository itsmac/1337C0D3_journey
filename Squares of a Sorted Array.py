'''
No: 977. 
Title: Squares of a Sorted Array
'''


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l,r = 0,len(A)-1
        res = [0]*len(A)
        while(l<=r):
            if abs(A[l]) > abs(A[r]):
                res[r-l] = A[l] ** 2
                l+=1
            else:
                res[r-l] = A[r] ** 2
                r-=1
        return res

'''
Checking for largest and inserting in the arr in appropriate pos r-l
'''
            
