#
# @lc app=leetcode id=311 lang=python3
#
# [311] Spare Matrix Multiplication
#

# @lc code=start
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        
        mat = [[0 for _ in range(l)] for _ in range(m)]
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in enumerate(B[k]):
                        if eleB: 
                            mat[i][j] += eleA * eleB
        return mat
# @lc code=end

