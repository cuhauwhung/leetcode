#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # di and dj is to change the directions 
        ans = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        
        for k in range(n*n):
            ans[i][j] = k + 1

            # whenever we meet a corner, which is represented by a cell that is not 0, we switch 
            if ans[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di

            i += di
            j += dj

        return ans

# @lc code=end

