#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        # key: use prefix sum         
        #      Let P[i+1] = A[0] + A[1] + ... + A[i]. Then, each subarray can be written as P[j] - P[i] (for j > i). Thus, we have P[j] - P[i] equal to 0 modulo K, or equivalently P[i] and P[j] are the same value modulo K. Keep track of values of modulo seen before and increment counts

        count = summ = 0  
        dic = {0: 1}

        for a in A:
            summ = (summ + a) % K 

            if summ in dic:
                count += dic[summ]
                dic[summ] += 1 
            else:
                dic[summ] = 1

        return count 
                
# @lc code=end