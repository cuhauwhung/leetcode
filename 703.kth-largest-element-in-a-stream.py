#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:

    # key: make heap but only let it have k-largest elements by popping off small elements 
    # With only k elements, the smallest item (self.pool[0]) will always be the kth largest.
    # If a new value is bigger than the smallest, it should be added into your heap
    # If it's bigger than the smallest (that are already the kth largest), it will certainly be within the kth largest of the stream.

    def __init__(self, k: int, nums: List[int]):
        self.pool = nums 
        self.k = k 
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)
        
    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)

        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)

        return self.pool[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
