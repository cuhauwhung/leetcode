#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:

        path_array = [p for p in path.split("/") if p!="." and p!=""]
        stack = [] 

        for cur in path_array:
            if cur == "..":
                if len(stack) > 0:
                    stack.pop()    
            else:
                stack.append(cur) 

        return "/" + "/".join(stack) 
# @lc code=end