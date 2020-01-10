#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, v in enumerate(nums): 
            remain = target - v 
            if remain in seen:
                return [seen[remain], i]
            seen[v] = i 
        return []
        
# @lc code=end

