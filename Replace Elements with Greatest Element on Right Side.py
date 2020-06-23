'''
No: 1299. 
Title: Replace Elements with Greatest Element on Right Side
Level: Easy
'''


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) -1
        a = [-1]
        max_val = 0
        while i >= 0:
            if arr[i] > max_val:
                max_val = arr[i]
            a.append(max_val)
            i-=1
        a.pop()
        return a[::-1]
        
'''
traverse from right to left
get the max val and append it to the list or append the existing max val
return reverse of the list
'''
