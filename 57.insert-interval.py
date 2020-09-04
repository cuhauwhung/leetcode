#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # key: same as 56. merge intervals, but just append the newInterval into intervals
        
        out = list()
        intervals.append(newInterval)
        for i in sorted(intervals, key = lambda i: i[0]):
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            else:
                out.append(i)
        return out 
# @lc code=end

