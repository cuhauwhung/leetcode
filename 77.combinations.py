#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(nums, k, s, curr, ans, seen):
            if len(curr) == k:
                curr.sort()
                temp = tuple(curr)
                if temp not in seen:
                    seen.add(temp)
                    ans.append(curr[:])
                    return

            for i in range(s, len(nums)):
                curr.append(nums[i])
                dfs(nums, k, i+1, curr, ans, seen)
                curr.pop()

        ans, seen = list(), set()
        nums = [i for i in range(1, n+1)]
        dfs(nums, k, 0, [], ans, seen)
        return ans
        
# @lc code=end
