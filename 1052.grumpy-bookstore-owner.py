#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        
        # deals with customers that are already satisfied
        already_satisfied = 0 
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                already_satisfied += customers[i]
                customers[i] = 0 

        # deals with optimizing customers that are not satisfied
        opt_satisfied = 0
        current_satisfied = 0
        for i, customers_at_time in enumerate(customers):
            current_satisfied += customers_at_time

            # remove satisfied customers, because they are out of the range
            if i >= X: 
                current_satisfied -= customers[i - X]
            opt_satisfied = max(opt_satisfied, current_satisfied)

        return opt_satisfied + already_satisfied
# @lc code=end

