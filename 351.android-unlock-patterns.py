#
# @lc app=leetcode id=351 lang=python3
#
# [351] Android Unlock Patterns
#

# @lc code=start
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:

        def make_skips():
            skip = [[0] * 10 for _ in range(10)]
            skip[1][3] = skip[3][1] = 2
            skip[1][7] = skip[7][1] = 4
            skip[3][9] = skip[9][3] = 6
            skip[7][9] = skip[9][7] = 8
            skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
            return skip

        def dfs(curr, pattern_len):
            
            if pattern_len < 0: return 0
            if pattern_len == 0: return 1
            visited[curr] = True
            count = 0 
            for num in range(1, 10):
                if not visited[num] and (skip[curr][num] == 0 or visited[skip[curr][num]]):
                    count += dfs(num, pattern_len - 1)
            visited[curr] = False
            return count             


        skip = make_skips()
        visited = [False] * 10
        ans = 0 
        for pattern_len in range(m, n+1):
            ans += dfs(1, pattern_len - 1) * 4
            ans += dfs(2, pattern_len - 1) * 4
            ans += dfs(5, pattern_len - 1)
        return ans
       
      
# @lc code=end

