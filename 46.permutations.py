#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, curr, ans):

            # no more nums means path is full 
            if not len(nums):
                ans.append(curr[:])
                return 
                
            for i in range(len(nums)):
                new_nums = nums[:i] + nums[i+1:]
                curr.append(nums[i])
                dfs(new_nums, curr, ans)
                curr.pop()

        ans = list()
        dfs(nums, [], ans)

        return ans 

# @lc code=end

