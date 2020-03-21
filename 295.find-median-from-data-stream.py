#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.numbers = list()

    def addNum(self, num: int) -> None:
        bisect.insort(self.numbers, num)

    def findMedian(self) -> float:
        nums = self.numbers
        if len(nums) % 2 == 0:
            return (nums[len(nums)//2] + nums[len(nums)//2-1]) / 2.0
        else:
            return nums[len(nums)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

