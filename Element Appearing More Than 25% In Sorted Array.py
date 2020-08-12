'''
1287. 
Element Appearing More Than 25% In Sorted Array
Easy
'''

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num = len(arr)
        if num == 1:
            return arr[0]
        target = [arr[num//4],arr[num//2],arr[(3*num)//4]]
        def first_occurrence(a, hit):
            l = 0
            r = len(arr) - 1
            while (l < r):
                mid = l + (r - l) // 2
                if a[mid] == hit and ( mid == l  or a[mid - 1] < hit):
                    return mid
                elif a[mid] < hit:
                    l = mid + 1
                else:
                    r = mid

        for i in target:
            left = first_occurrence(arr, i)
            k = left + num//4
            if i == arr[k]:
                return i
        
