#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # # O(nlgn) time
        # nums.sort()
        # return nums[-k] 

        # O(k+(n-k)lgk) time, min-heap
        heapq.heapify(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

# @lc code=end