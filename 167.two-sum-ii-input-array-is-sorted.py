#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff = dict()
        ans = list()
        for i, x in enumerate(numbers):
            if x in diff:
                ans = [i+1, diff[x]]
            else:
                diff[target-x] = i+1
        return sorted(ans)

# @lc code=end

