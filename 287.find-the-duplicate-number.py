#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = seeker = 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                while seeker != slow:
                    seeker = nums[seeker]
                    slow = nums[slow]
                return seeker

# @lc code=end

