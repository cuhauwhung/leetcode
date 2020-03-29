#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # key: idea same to 3sum, but keep track of 2 indexes
        res = set(tuple())
        rightmost = len(nums) - 1
        nums.sort()

        for i in range(len(nums)):            
            for j in range(i+1, len(nums)):
                
                left = j + 1 
                right = rightmost
                
                while left < right:
                    
                    cur_sum = nums[left] + nums[right] + nums[i] + nums[j]
                    
                    if cur_sum < target: 
                        left += 1
                    
                    elif cur_sum > target:
                        right -= 1
                        
                    else:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
        return res 
# @lc code=end

