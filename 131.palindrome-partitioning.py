#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_pal(s):
            return s == s[::-1]
        
        def dfs(s, curr, ans):
            if not s:
                ans.append(curr[:])
                return 

            for i in range(1, len(s)+1):
                if is_pal(s[:i]):
                    curr.append(s[:i])
                    dfs(s[i:], curr, ans)
                    curr.pop()

        ans = list()
        dfs(s, [], ans)
        return ans 

# @lc code=end

