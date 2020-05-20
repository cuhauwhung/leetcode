#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        emps = {employee.id: employee for employee in employees}

        def dfs(id):
            ans = emps[id].importance
            for sub_id in emps[id].subordinates:
                ans += dfs(sub_id)
            return ans 
        return dfs(id)
        
# @lc code=end