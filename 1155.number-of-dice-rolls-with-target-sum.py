#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        # key: use DP 
        #      

        dp = [1] + [0] * target
        for _ in range(d):
            for j in range(target, -1, -1):
                # min(f, j) go until the # of faces or j 
                # dp[j] = # of ways we can get j with given # of dices 
                dp[j] = sum([dp[j - k] for k in range(1, 1 + min(f, j))] or [0])
        return dp[target] % (10**9 + 7)
# @lc code=end

