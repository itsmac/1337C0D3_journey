'''
1356. 
Sort Integers by The Number of 1 Bits
Easy
'''


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        def count_bits(n):
            ct = 0
            while(n):
                n = n & n-1
                ct+=1
            return ct
        
        d = {}
        for i in arr:
            count = count_bits(i)
            if count not in d:             
                d[count] = [i]
            else:
                d[count].append(i)
        print(d)
        
        for i in sorted(d.keys()):
            res.extend(sorted(d[i]))
        return res
        
        
'''
Better solution can be done
'''
