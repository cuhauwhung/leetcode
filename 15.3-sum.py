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
                
                # sum is > 0, increase left 
                elif check_sum < 0: 
                    left += 1
                
                # sum is < 0 decrease right 
                else: 
                    right -= 1
        
        return result

        # PRODUCES CORRECT RESULT, BUT NOT ACCEPTED BY LEETCODE DUE TO TIME
        # use dfs and only add it to the list of answers if the sum = 0 and if length = 3 
        # def dfs(nums, s, curr, ans, seen):
            
        #     if len(curr) == 3 and sum(curr) == 0:
        #         if tuple(curr) not in seen:
        #             ans.append(curr[:])
        #             seen.add(tuple(curr))

        #     for i in range(s, len(nums)):

        #         if len(curr) >= 3:
        #             return

        #         curr.append(nums[i])
        #         dfs(nums, i+1, curr, ans, seen)
        #         curr.pop()

        # ans = list()
        # seen = set()
        # nums.sort()
        # dfs(nums, 0, [], ans, seen)
        # return ans  


# @lc code=end

