#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        # key: use DP / greedy 
        #      dp[i] is the length of wiggle subsequence at i 
        #      keep track of two variables up and down. 
        #      at each index, we have three choices: up, down and equal
        #      if up: down + 1, elif down: up + 1 
        
        if len(nums) == 0: return 0
        up = down = 1 
        for i in range(1, len(nums)):

            # down 
            if nums[i] < nums[i-1]:
                down = up + 1 
            
            # up 
            elif nums[i] > nums[i-1]:
                up = down + 1 

        return max(up, down)
        
# @lc code=end