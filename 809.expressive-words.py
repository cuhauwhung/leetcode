#
# @lc app=leetcode id=809 lang=python3
#
# [809] Expressive Words
#

# @lc code=start
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        # key: perform grouping by each char and then check if they fit constraints 
        return sum(self.check(S, W) for W in words)

    def check(self, S, W):

        i, j, i2, j2, n, m = 0, 0, 0, 0, len(S), len(W)
        while i < n and j < m:
            
            if S[i] != W[j]: return False 
            while i2 < n and S[i] == S[i2]: i2 += 1 
            while j2 < m and W[j] == W[j2]: j2 += 1 

            # if there is difference between dist_J and dist_S
            # if dist_S is < max(3, dist_J) 
            if i2 - i != j2 - j and i2 - i < max(3, j2 - j):
                return False 

            i = i2 
            j = j2 

        return i == n and j == m 

# @lc code=end

