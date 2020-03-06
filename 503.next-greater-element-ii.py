#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack = []
        ans = [-1] * len(nums)

        for i in list(range(len(nums))) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                t = stack.pop()
                ans[t] = nums[i]
            stack.append(i)
        return ans 

# @lc code=end

