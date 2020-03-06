#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        ans, prefix, i  = list(), "", 0

        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            ans.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        return ans 

# @lc code=end