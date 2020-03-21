#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math 

        # key idea: essentially, the original list would have n! entries,
        #           for each number beginning with x we would have (n-1)! entries.
        
        numbers = [i for i in range(1, n+1)]
        permutation = ''
        k -= 1

        while n > 0:
            
            n -= 1

            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])

            # remove handled number
            numbers.remove(numbers[index])

        return permutation

        # @lc code=end