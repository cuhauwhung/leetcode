#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        # key: each dp[i] would be the subset that has the pairs satisfied, if nums[i] % nums[j], then we just add nums[i] to dp[j], giving us dp[i]

        nums.sort()
        if len(nums) == 0: return []
        result = [nums[0]]
        dp = [[i] for i in nums]

        for i in range(len(dp)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
            
            if len(dp[i]) > len(result):
                result = dp[i]

        return result

# @lc code=end