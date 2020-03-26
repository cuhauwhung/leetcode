#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        # key: 
        # If the original string has a repeating substring, the repeating substring can be no larger than 1/2 the length of the original string. I.e "xyxy" would be "xy"
        # By repeating the string and removing the first and last character of the new string, I.e "xyxyxyxy" => "yxyxyx", if the original string "xyxy" can be found in "yxyxyx", it means that "xyxy" has a repeating substring.

        if not s:
            return False

        ss = (s+s)[1:-1]
        return ss.find(s) != -1 




# @lc code=end

