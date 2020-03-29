#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#

# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        
        # key: use kadane's algorithm with CDF
        #      keep track of Lmax/Mmax (prefix sum with length L/M)
        #      add to the other 'half' to get max sum 

        # CDF
        for i in range(1, len(A)):
            A[i] += A[i-1]

        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]

        # | ---- L ---- | ---- M ---- | (i)
        for i in range(L+M, len(A)):
            Lmax = max(Lmax, A[i-M] - A[i-L-M])
            res = max(res, Lmax + A[i] - A[i-M])

        # | ---- M ---- | ---- L ---- | (i)
        for i in range(L+M, len(A)):
            Mmax = max(Mmax, A[i-L] - A[i-L-M])
            res = max(res, Mmax + A[i] - A[i-L])

        return res 

# @lc code=end