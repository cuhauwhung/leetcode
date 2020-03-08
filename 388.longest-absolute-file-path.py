#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:

        max_len = 0
        path_len = {0: 0}
        split_lines = input.splitlines()

        for cur in split_lines:
            name = cur.lstrip("\t")
            depth = len(cur) - len(name)

            if "." in name:
                max_len = max(max_len, path_len[depth] + len(name))

            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1

        return max_len
# @lc code=end

