'''
No: 832. 
Title: Flipping an Image
Level: Easy
'''


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            right = len(i)-1
            left = 0
            while(left<=right): 
                if left == right:
                    i[left] ^=1
                    break                    
                i[left],i[right] = i[right]^1,i[left]^1
                left+=1
                right-=1
        return A
    
                
'''
Note: Flipping means reversing the rows and make complement
So I swap and ^1 for every element
'''
                
        
