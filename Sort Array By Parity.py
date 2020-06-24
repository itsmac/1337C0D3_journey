'''
No: 905. 
Title: Sort Array By Parity
Level: Easy
'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A)-1
        while(left<right):
            if A[left] %2 != 0 and A[right]%2 == 0:
                A[left],A[right] = A[right],A[left]
            if A[left] %2 != 0  and A[right]%2 != 0:
                right-=1
            if A[left] %2 == 0:
                left+=1
                
        return A

'''
In place swap. 
'''
            
