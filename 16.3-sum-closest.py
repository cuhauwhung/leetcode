#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
    
        # key: just like 3sum, but have to find smallest distance 
        
        ans = float('Inf')
        nums.sort()
        rightmost = len(nums) -1 
        for index, eachNum in enumerate(nums):
            left = index + 1 
            right = rightmost
            
            while left < right: 
                checkSum = eachNum + nums[left] + nums[right] 
                
                if checkSum == target:
                    return checkSum 
                
                if abs(checkSum - target) < abs(ans - target):
                    ans = checkSum
                    
                if checkSum < target:
                    left += 1 
                
                elif checkSum > target:
                    right -= 1 
                    
        return ans 
# @lc code=end