#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, s, curr, ans):
            
            ans.append(curr[:])
            
            for i in range(s, len(nums)):
                curr.append(nums[i])
                dfs(nums, i+1, curr, ans)
                curr.pop()
            
        ans = list()
        dfs(nums, 0, [], ans)
        return ans
# @lc code=end

