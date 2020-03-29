#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#

# @lc code=start


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        # key: if (i,j,k) works, then (i,j,k), (i,j,k-1),..., 
        #      (i,j,j+1) all work, totally (k-j) triplets

        count = 0
        nums.sort()
        rightmost = len(nums) - 1 
        
        for idx, eachNum in enumerate(nums):
            
            left = idx + 1 
            right = rightmost 
            
            while left < right: 
                
                checkSum = eachNum + nums[left] + nums[right]
          
                if checkSum < target:
                    count += right - left
                    left += 1
                    
                else: 
                    right -= 1
        
        return count

# @lc code=end