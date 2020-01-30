#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        target = sum(nums)/k
        nums.sort(reverse = True)
        visited = [0] * n

        def DFS(k, index, curr_sum):

            if k == 1:  
                return True

            if curr_sum == target: 
                return DFS(k-1, 0, 0) 

            for i in range(index, n):
                if not visited[i] and nums[i] + curr_sum <= target:
                    visited[i] = 1
                    if DFS(k, i + 1, curr_sum + nums[i]):
                        return True
                    visited[i] = 0

            return False
            
        return DFS(k,0,0)    



# @lc code=end

