#
# @lc app=leetcode id=755 lang=python3
#
# [755] Pour Water
#

class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
                
        for _ in range(V):
            
            index = K 
            
            # go left and find good spot 
            for i in range(K-1, -1, -1):
                if heights[i] > heights[i+1]:
                    break
                elif heights[i] < heights[i+1]:
                    index = i
                    
            if index != K:
                heights[index] += 1 
                continue 
                
            for i in range(K+1, len(heights)):
                if heights[i] > heights[i-1]:
                    break
                elif heights[i] < heights[i-1]:
                    index = i
                    
            heights[index] += 1 
                
        return heights

# @lc code=start
