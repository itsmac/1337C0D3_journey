'''
No: 1304
Title: Find N Unique Integers Sum up to Zero
Level: Easy
'''


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        # i = 0 
        # val = n // 2
        # for i in range(-val,val+1):
        #     if n%2 == 0 and i is not 0:
        #         res.append(i)
        #     if n%2 !=0:
        #         res.append(i)
        # return res
        for i in range(n):
            res.append(i*2-n+1)
        return res

'''
Note derive the formula:
-->   i*2-n+1
if n = 5 [-4,-2,0,2,4]
if n = 3 [-2,0,2]

Also finish the proble by using range(1-n,n,2)
'''
