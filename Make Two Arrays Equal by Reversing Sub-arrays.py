'''
No: 1460. 
Title: Make Two Arrays Equal by Reversing Sub-arrays
Level: Easy
'''

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr_dict = {}
        for i in arr:
            if i not in arr_dict:
                arr_dict[i] = 1
            else:
                arr_dict[i] +=1
        
        for i in target:
            if arr_dict.get(i) is None or arr_dict[i]  <= 0:
                return False
            elif arr_dict[i] > 0:
                arr_dict[i] -=1
        return True
'''
initially store the values in dictioanry with their count.
if we have target values in dict then decrement
if it does not then return false since every element needs to be present in both the lists to recreate
'''
            
            
                
        
            
        
        
