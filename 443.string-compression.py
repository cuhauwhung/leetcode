#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        # key: use two pointers 
        #      group array into repeated chunks, keep track of char and count, then modify original array with the new info 

        left = i = 0 
        while i < len(chars):
            cur_char, cur_len = chars[i], 1 
            while (i+1) < len(chars) and cur_char == chars[i+1]:
                cur_len, i = cur_len + 1, i + 1 
            
            chars[left] = cur_char 
            if cur_len > 1:
                len_str = str(cur_len)
                chars[left + 1: left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i+ 1 
            
        return left 
