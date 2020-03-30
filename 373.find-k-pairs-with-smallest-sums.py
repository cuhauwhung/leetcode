#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # key: keep heap of length 3 and keep replacing the root 
        # with pop and fill it with new sum(vals) if root > sum(vals) 
        heap = []
        for n1 in nums1:
            for n2 in nums2: 
                if len(heap) < k:
                    heapq.heappush(heap, (-n1-n2, [n1,n2]))

                else:
                    if heap and -heap[0][0] > n1 + n2:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-n1-n2, [n1, n2]))
                    else:
                        break
        return [heapq.heappop(heap)[1] for _ in range(k) if heap]



                
# @lc code=end

