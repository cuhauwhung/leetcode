#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone_map = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}

        def dfs(nums, phone_map, s, curr, ans):

            if len(curr) == len(nums):
                ans.append("".join(curr[:]))
                return

            for j in phone_map[digits[s]]:
                curr.append(j)
                dfs(digits, phone_map, s+1, curr, ans)
                curr.pop()

        if not digits: return []
        ans = list()
        dfs(digits, phone_map, 0, [], ans)
        return ans
        
# @lc code=end