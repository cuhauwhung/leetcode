#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        ans = anchor = 0

        for i in range(len(A)):
            if i >= 2 and (A[i-2] > A[i-1] < A[i] or A[i-2] < A[i-1] > A[i]):
                anchor += 1
            elif i >= 1 and A[i-1] != A[i]:
                anchor = 2
            else:
                anchor = 1
            ans = max(ans, anchor)
        return ans
# @lc code=end

