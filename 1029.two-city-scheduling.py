#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sort_1 = sorted(costs, key = lambda x: x[0] - x[1]) 
        total = 0 
        n = len(costs) // 2
        
        for i in range(n):
            total += sort_1[i][0] + sort_1[i+n][1]
        return total 
# @lc code=end