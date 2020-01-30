#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        

        # res = need = 0
        # for i in sorted(A):
        #     res += max(need - i, 0)
        #     print("res: --" + str(res))
        #     need = max(need + 1, i + 1)
        #     print("need: -- " + str(need))

        # return res

        # idea: o(log n)
        from collections import Counter 
        count = Counter(A)
        nums_new_home = []

        ans = 0
        for x in range(100000):
            
            if count[x] >= 2:
                nums_new_home.extend([x] * (count[x] -1 ))

            elif nums_new_home and count[x] == 0:
                ans += x - nums_new_home.pop()

        return ans 


# @lc code=end

