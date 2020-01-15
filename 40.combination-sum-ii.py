#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, target, s, ans, curr):
            if target == 0:
                ans.append(curr[:])
                return 
            
            for i in range(s, len(candidates)):
                num = candidates[i]

                if num > target: return 

                curr.append(num)
                dfs(candidates, target - num, i + 1, ans, curr)
                curr.pop()

        ans = list()
        candidates.sort()
        dfs(candidates, target, 0, ans, [])
 
        ans = list(set(tuple(row) for row in ans))

        return ans


# this is essentially thes ame as leetcode 39, but the only different is that you can only use a number once 
# hence, the differences are: 1) when calling dfs, you start with a +1 position and at the end you have to remove duplicate answers



       

# @lc code=end

