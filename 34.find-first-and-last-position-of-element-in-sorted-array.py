#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # key: use binary search twice. Once to find left and second to find right (lb # and ub )
        # when searching right, 
        # we want to keep pushing right thats why there is the equal sign  

        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = int((left + right) / 2)
                if target > nums[mid]: left = mid + 1
                else: right = mid - 1
            return left

        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = int((left + right) / 2)
                if target >= nums[mid]: left = mid + 1
                else: right = mid - 1
            return right
            
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]

# @lc code=end

