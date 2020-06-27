#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if stack == [] or mapping[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


# @lc code=end


