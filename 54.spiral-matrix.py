#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        if not matrix:
            return []

        m, n = len(matrix),len(matrix[0])
        i,j,di,dj = 0,0,0,1
        
        for _ in range(m * n):

            # after we append into list, we modify it to ''
            res.append(matrix[i][j])
            matrix[i][j] = ''

            # if the values are going out of bounds, then switch direction
            if matrix[(i + di) % m][(j + dj) % n] == '':
                di, dj = dj, -di

            i += di
            j += dj

        return res

# @lc code=end

