#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        from collections import defaultdict
        if not nums: return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}

        for i in range(1, len(nums)):
            temp_dict = defaultdict(int)

            for val, count in dic.items():
                temp_dict[val + nums[i]] = temp_dict[val + nums[i]] + count
                temp_dict[val - nums[i]] = temp_dict[val - nums[i]] + count
            dic = temp_dict
        
        return dic.get(S, 0)
        
# @lc code=end

