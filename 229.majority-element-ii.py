#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter 
        count = Counter(nums)
        return [num for num in count if count[num] > (len(nums) // 3)]

# @lc code=end

