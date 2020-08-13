'''
1170. 
Compare Strings by Frequency of the Smallest Character
Easy
'''

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        q = []
        w = []
        res = []
        for i in queries:
            min_element = float('Inf')
            for j in i:
                if ord(j) < min_element:
                    min_element = ord(j)            
            q.append(i.count(chr(min_element)))
        
        for i in words:
            min_element = float('Inf')
            for j in i:
                if ord(j) < min_element:
                    min_element = ord(j)            
            w.append(i.count(chr(min_element)))
        
        for i in q:
            cnt = 0
            for j in w:
                if i<j:
                    cnt+=1
            res.append(cnt)
        return res
        
'''
TO Do:
Reduce the runtime or change the approach for the program
'''
            
                    
                    
                
        
            
                    
        
