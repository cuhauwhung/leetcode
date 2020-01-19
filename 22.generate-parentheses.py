#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(left, right, ans, string):
            if right < left: return
            if not left and not right:
                ans.append(string)
                return
                
            if left:
                dfs(left-1, right, ans, string + "(")

            if right:
                dfs(left, right-1, ans, string + ")")

        if not n: return []
        ans = list()
        dfs(n, n, ans, "")
        return ans
# @lc code=end

