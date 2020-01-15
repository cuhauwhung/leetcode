#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, target, s, curr, ans):
            if target == 0:
                ans.append(curr[:])
                return

            for i in range(s, len(candidates)):

                num = candidates[i] 

                # this combination doesn't work
                if num > target: return 

                # this combination has room to test out somemore 
                curr.append(num)
                dfs(candidates, target - num, i, curr, ans)
                curr.pop()

        ans = list()
        candidates.sort()

        # s is the marker to determine where we are on the candidates 
        dfs(candidates, target, 0, [], ans)

        
        return ans

# @lc code=end

