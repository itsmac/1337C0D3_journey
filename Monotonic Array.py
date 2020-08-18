'''
896. 
Monotonic Array
Easy
'''

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = False
        dec = False
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                if dec is True:
                    return False
                inc = True
            elif A[i] < A[i+1]:
                if inc is True:
                    return False
                dec = True
            else:
                continue
        return True
            
            
        
