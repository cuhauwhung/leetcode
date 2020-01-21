#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:


        # key idea: we obtain count_a and count_b, then iterate through each number 1 by 1. If the count of a number at both lists - same == N, then that this total can fill up the length of the array, which means that we can perform rotations to get top or bottom all the same 
        from collections import defaultdict

        count_a = defaultdict(int)
        count_b = defaultdict(int)
        N = len(A)
        same = 0

        for i in range(N):
            count_a[A[i]] += 1
            count_b[B[i]] += 1

            if A[i] == B[i]:
                same += 1

        for x in range(1,7):
            if (count_a[x] + count_b[x] - same) == N:
                return N - max(count_a[x], count_b[x])

        return -1

# @lc code=end

