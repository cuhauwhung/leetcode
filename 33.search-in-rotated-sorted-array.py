#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # idea: if its complete order, we can totally rule out one half 
        # but if its not, then we have to see which half we have to perform the binary search at 

        # recursive method 
        def binary_search(nums, left, right, target):

            if left > right: return -1 
            mid = int(left + (right - left) / 2)

            if target == nums[mid]: return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    return binary_search(nums, left, mid - 1, target)
                else:
                    return binary_search(nums, mid + 1, right, target)
            else:
                if nums[mid] < target and target <= nums[right]:
                    return binary_search(nums, mid + 1, right, target)
                else:
                    return binary_search(nums, left, mid - 1, target)

        return binary_search(nums, 0, len(nums)-1, target)

        # # iterative method 
        # left = 0 
        # right = len(nums) - 1 

        # while left <= right:

        #     mid = int(left + (right - left) / 2)
        #     if target == nums[mid]: return mid 

        #     if nums[left] <= nums[mid]:
        #         if nums[left] <= target and target < nums[mid]:
        #             right = mid - 1 
        #         else:
        #             left = mid + 1 
        #     else:
        #         if nums[mid] < target and target <= nums[right]:
        #             left = mid + 1 
        #         else:
        #             right = mid - 1 

        # return -1 

# @lc code=end

