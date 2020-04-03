#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#

# @lc code=start
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:

        # key: Find the index i of the next maximum number x.
        #      Reverse i + 1 numbers, so that the x will be at A[0]
        #      Reverse x numbers, so that x will be at A[x - 1].
        #      Repeat this process N times.

        res = list()
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res

# @lc code=end
