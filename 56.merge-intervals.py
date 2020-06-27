#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # key: sort intervals by start time 
        #      if can't combine, add new interval
        #      if can extend then take the max end time of both intervals  

        out = list()
        for i in sorted(intervals, key = lambda i: i[0]):
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            else:
                out.append(i)
        return out 

# @lc code=end

