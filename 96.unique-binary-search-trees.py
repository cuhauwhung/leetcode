#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:

        # idea: remember F(3,7) = G(2) * G(4) 
        #       and G[i] = sum(G(i)) for i in 1 to n

        G = [0]*(n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j-1] * G[i-j]

        return G[n]
        



# @lc code=end

