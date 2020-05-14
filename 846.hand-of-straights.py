#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        from collections import Counter 
        from heapq import heappop, heapify

        l, count = len(hand), Counter(hand)
        if l % W: return False
        if W == 1: return True 

        # build heap 
        heapify(hand)

        # loop to the number of elements in each group 
        for _ in range(l // W):

            # try to find the min value in each group and keep popping if 
            # it is not available 
            start = heappop(hand)
            
            while count[start] == 0:
                start = heappop(hand)
            
            # find the other numbers in the group 
            for _ in range(W):

                # can't find the min number in the group, return False 
                if not count[start]: return False 
                count[start] -= 1 
                start += 1 
        
        return True 

# @lc code=end