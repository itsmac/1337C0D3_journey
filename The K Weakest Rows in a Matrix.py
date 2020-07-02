'''
No: 1337. 
Title: The K Weakest Rows in a Matrix
'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dict_val = {}
        res = []
        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if j is 0:
                    break
                count+=1
            dict_val[i] = count
        key_list = list(dict_val.keys())
        val_list = list(dict_val.values())
        for _ in range(k):
            index_val = val_list.index(min(val_list))
            res.append(key_list[index_val])
            key_list.remove(key_list[index_val])
            val_list.pop(index_val)
        return res
            
            
'''
solution can be improved. 
'''
