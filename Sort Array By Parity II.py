'''
No: 922. 
Title: Sort Array By Parity II
'''


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        even,odd = 0,1
        i = 0
        while(i<len(A)):
            if A[i] %2 == 0:
                res[even] = A[i] 
                even +=2
            else:
                res[odd] = A[i]
                odd+=2
            i+=1
        return res
                
            
            
'''
check for the val,
if its odd insert at odd and increase the odd index by 2
if its odd insert at even and increase the even index by 2
'''
