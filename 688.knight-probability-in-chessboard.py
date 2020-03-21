#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#

# @lc code=start
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        # Let f[r][c][n] be the probability of being on square (r, c) after n-steps

        moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1

        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in moves:
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0

            dp = dp2
        return sum(map(sum, dp))
# @lc code=end

