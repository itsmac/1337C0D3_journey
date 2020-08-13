'''
888. 
Fair Candy Swap
Easy
'''


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a,sum_b = sum(A),sum(B)
        temp = set(B)
        for i in A:
            k = i + (sum_b - sum_a)//2
            if k in temp:
                return [i,k]

'''
x -> alice swap candy
y -> bob to return back
SA−x+y=SB−y+x
y=x+(SB−SA/2)
'''
