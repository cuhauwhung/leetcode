#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        return list(heapq.merge(*matrix))[k-1]

        # elements = list()
        # for row in matrix:
        #     for x in row:
        #         elements.append(x)
        # elements.sort()
        # return elements[k - 1] 
# @lc code=end

