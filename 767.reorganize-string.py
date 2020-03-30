#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    def reorganizeString(self, S: str) -> str:

        # key: check if any one of the chars takes up more than half 
        # of the possible array; if yes, return "". If no, then we can fit it 
        # into the array alternating [a _ a _ a _], interleaving with the other chars

        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)/2: return ""
            A.extend(c * x)

        ans = [None] * N
        ans[::2] = A[N//2:]
        ans[1::2] = A[:N//2]

        return "".join(ans)

# @lc code=end

