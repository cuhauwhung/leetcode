#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anangram = dict()
        for word in sorted(strs):
            key = tuple(sorted(word))
            anangram[key] = anangram.get(key, []) + [word]
        return anangram.values()

# @lc code=end

