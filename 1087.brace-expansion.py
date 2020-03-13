#
# @lc app=leetcode id=1087 lang=python3
#
# [1087] Brace Expansion
#

class Solution:
    def expand(self, S: str) -> List[str]:
                
        def dfs(s, word, ans):
            if not s:
                ans.append(word)

            else:
                if s[0] == "{":
                    i = s.find("}")
                    for c in s[1:i].split(","):
                        dfs(s[i+1:], word + c, ans)
                
                else:
                    dfs(s[1:], word + s[0], ans)

        ans = list()
        dfs(S, "", ans)
        ans.sort()
        return ans

# @lc code=end