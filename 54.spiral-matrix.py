#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        if not matrix: return []
        m, n = len(matrix),len(matrix[0])

        i,j,di,dj = 0,0,0,1
        
        for _ in range(m * n):

            # after we append into list, we modify it to ''
            res.append(matrix[i][j])
            matrix[i][j] = ''

             # (i+di) or (j+dj) is the next visit and if it reaches the boundary
             # %m will bring it back to the 1st element of the column/row, which has to be ''.
            if matrix[(i + di) % m][(j + dj) % n] == '':
                di, dj = dj, -di

            i += di
            j += dj

        return res

# @lc code=end

