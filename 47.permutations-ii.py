#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # key: we have to use dfs, but we have to remember the visited indexes
        #       the visited is to prevent the curr 

        # def dfs(nums, visited, curr, ans):

        #     if len(nums) == len(curr):
        #         ans.append(curr[:])
        #         return 

        #     for i in range(len(nums)):

        #         if visited[i]:
        #             continue 

        #         # prune solution space 
        #         if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
        #             continue
                
        #         visited[i] = 1 
        #         curr.append(nums[i])
        #         dfs(nums, visited, curr, ans)
        #         curr.pop()
        #         visited[i] = 0

        # ans, visited = list(), [0] * len(nums)
        # nums.sort()
        # dfs(nums, visited, [], ans)
        # return ans 

    
        def dfs(nums, curr, res):
            if not nums:
                res.append(curr[:])
                return 

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                new_nums = nums[:i] + nums[i+1:]
                curr.append(nums[i])
                dfs(new_nums, curr, res)
                curr.pop()

        res = list()
        nums.sort()
        dfs(nums, [], res)
        return res

# @lc code=end

