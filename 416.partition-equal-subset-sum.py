#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
           
        n, memo = len(nums), {0: True}
        nums.sort(reverse=True)
        if sum(nums) & 1: return False

        def dfs(i, x):
            if x not in memo:
                memo[x] = False 
                if x > 0:
                    for j in range(i, n):
                        if dfs(j + 1, x - nums[j]):
                            memo[x] = True
                            break
            return memo[x]

        return dfs(0, sum(nums) >> 1)  
# @lc code=end

