'''
No: 1491. 
Title: Average Salary Excluding the Minimum and Maximum Salary
'''


class Solution:
    def average(self, salary: List[int]) -> float:
        val = 0
        max_val,min_val = max(salary),min(salary)
        for i in salary:
            val += i
        return (val-max_val-min_val)/(len(salary)-2)
        


'''
find the max and min
subtract the above val in total and find the mean
'''
