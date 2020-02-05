#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = list()
        i, j = 0, 0
        
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i+1] == nums[i]+1:
                continue 
                
            if i == j:
                ans.append(str(nums[i]))
            else:
                ans.append(str(nums[j]) + "->" + str(nums[i]))
            j = i + 1
        
        return ans 
# @lc code=end

