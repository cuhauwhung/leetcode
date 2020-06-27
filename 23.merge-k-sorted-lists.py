#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        # key: 
        #      use priority queue 
        #      use count to tie break same values 
        #      time= 0(nk log(k)) | n nodes, k lists, insert into heap takes log(k)
        #      space = 0(k) | only k nodes are stored at time 

        curr = head = ListNode(0)
        queue = [] 
        count = 0 
    
        for l in lists:
            if l:
                count += 1
                heapq.heappush(queue, (l.val, count, l))
        
        while queue: 
            _, _, curr.next = heapq.heappop(queue)
            curr = curr.next 

            if curr.next is not None:
                count += 1 
                heapq.heappush(queue, (curr.next.val, count, curr.next))

        return head.next 

# @lc code=end