#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # make placeholders
        product = [0] * (len(num1) + len(num2)) 
        position = len(product)-1 

        for n1 in num1[::-1]:
            tempPos = position 
            for n2 in num2[::-1]: 

                # mult. and bring carry over 
                product[tempPos] += int(n1) * int(n2) 
                product[tempPos-1] += product[tempPos]//10 
                product[tempPos] %= 10 
                
                # shift mult to the end of first integer
                tempPos -= 1 

            # once first integer is exhausted, shift second integer
            position -= 1 

        # when both integers are exhausted, make sure not padding zeros
        # pointer moves right and finds where zero padding stops
        pointer = 0
        while pointer < len(product)-1 and product[pointer] == 0: 
            pointer += 1

        return ''.join(map(str, product[pointer:])) # only report the digits to the right side of the pointer

# @lc code=end
