#
# @lc app=leetcode id=1177 lang=python3
#
# [1177] Can Make Palindrome from Substring
#

# @lc code=start
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        # prefix sum is the counts of each letter for given length
        prefix_sum = [[0] * 26]
        for i, char in enumerate(s):
            prefix_sum.append(prefix_sum[i][:])
            prefix_sum[i+1][ord(char) - ord('a')] += 1

        res = [True] * len(queries)
        for i, (start, end, k) in enumerate(queries):
            odd_count = 0 
            for j in range(26):
                odd_count += (prefix_sum[end+1][j] - prefix_sum[start][j]) % 2
            res[i] = (odd_count // 2) <= k

        return res 

        
# @lc code=end

