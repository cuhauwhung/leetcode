#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Sequence
#

# @lc code=start
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(dict)
        ans = 1

        for i in range(len(A)):
            for j in range(i):
                val = A[i] - A[j]
                d[i][val] = 1 + d[j].get(val, 1)
                ans = max(ans, d[i][val])
        return ans
    
# @lc code=end