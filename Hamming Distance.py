'''
461. 
Hamming Distance
Easy
'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x^y
        ct=0
        while a:
            # ct+=  a & 1 
            # a >>= 1
            ct+=1
            a = a & a-1
        return ct
        
        
        
        
'''
The commented portion is the naive approach
Brian kernighan  algo for counting set bits.... saves a lotta time.
Refer : https://www.techiedelight.com/brian-kernighans-algorithm-count-set-bits-integer/
'''
