#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        
        # key: use stack 
        #      store information about pervious sign 
        #      add num into stack. answer is sum of stack
        #       3+2*2 => {3}, {3,2}, {3, 2*2} = {3, 4} => ans = 7
        #       3 + 5/2 => {3}, {3,5}, {3, 5/2} = {3, 2} => ans = 5
        #       1 + 2*3 – 5 => {1}, {1,2}, {1,2*3} = {1,6}, {1, 6, -5} => ans = 2

        if not s: return "0"
        num, stack, prev_sign = 0, [], "+"

        for i in range(len(s)):

            if s[i].isdigit():
                num = num * 10 + int(s[i]) 

            if s[i] in "+-*/" or i == len(s) - 1:

                if prev_sign == "+":
                    stack.append(num)
                elif prev_sign == "-":
                    stack.append(-num)
                elif prev_sign == "*":
                    stack.append(num*stack.pop())
                elif prev_sign == "/":
                    stack.append(int(stack.pop()/num))
                
                num = 0 
                prev_sign = s[i]

        return sum(stack)
                
# @lc code=end