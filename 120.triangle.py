#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if not triangle: return 0 

        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]

            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j]) 

        return min(triangle[-1])




# @lc code=end

