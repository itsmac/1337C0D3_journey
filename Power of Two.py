'''
231. 
Power of Two
Easy
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ct = 0
        if n == 0:
            return False
        while n:
            n = n & n-1
            ct+=1
            if ct > 1:
                return False
        return True
