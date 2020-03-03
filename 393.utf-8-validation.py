#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0
        for d in data:
            if cnt:
                if d > 191 or d < 128: return False # 0xxxxxxx or 11xxxxxx
                cnt -= 1
            else:
                if d > 247: return False # 11111xxx -> more than 4 bytes
                if d > 239: cnt = 3 #11110xxx
                elif d > 223: cnt = 2 #1110xxxx
                elif d > 191: cnt = 1 #110xxxxx
                elif 0 <= d < 128: continue #0xxxxxxx
                else: return False;

        return not cnt

# @lc code=end

