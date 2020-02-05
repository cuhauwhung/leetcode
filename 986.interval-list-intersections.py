#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = list()
        pointerA, pointerB = 0, 0
        while pointerA < len(A) and pointerB < len(B):
            
            start_new = max(A[pointerA][0], B[pointerB][0])
            end_new = min(A[pointerA][1], B[pointerB][1])
            
            if start_new <= end_new:
                ans.append([start_new, end_new])
            
            if A[pointerA][1] < B[pointerB][1]:
                pointerA += 1
            else:
                pointerB += 1
                
        return ans 
# @lc code=end

