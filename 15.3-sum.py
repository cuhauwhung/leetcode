#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if nums is None: return None         
        result = set(tuple())
        nums.sort()
        rightmost = len(nums) - 1
        
        #Fix the first element, then search for the other two
        for index, eachNum in enumerate(nums):
            left = index + 1 
            right = rightmost
            
            while left < right: 
                check_sum = (eachNum + nums[left] + nums[right])
                
                # check if sum == 0 
                if check_sum == 0:
                    new_found = (eachNum, nums[left], nums[right])
                    if new_found not in result: 
                        result.add(tuple(new_found))
                    right -=1
                
                # sum is < 0, increase left 
                elif check_sum < 0: 
                    left += 1
                
                # sum is > 0 decrease right 
                else: 
                    right -= 1
        
        return result

# @lc code=end

