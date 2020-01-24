#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def dfs(s, index, curr, ans):
            if index == 4:
                if not s:
                    ans.append(curr[:-1])
                return 
            
            # number of digits to choose
            for i in range(1, 4):

                # digits chosen longer than length of s
                if i > len(s): return

                if int(s[:i]) <= 255:
                    dfs(s[i:], index + 1, curr + s[:i] + ".", ans)

                if s[0] == "0":
                    break

        ans = list()
        dfs(s, 0 , "", ans) 
        return ans 
# @lc code=end

