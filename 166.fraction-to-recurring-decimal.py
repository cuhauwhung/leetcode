#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        # key: dealing with no decimals is easy
        #           dealing with decimals is done by keeping track of the remainders 
        #           if the remainder appears again, this means that the div should be repeating
        
        res = list()
        if not denominator: return 
        if not numerator: return "0"        
        if (numerator < 0) ^ (denominator < 0): res.append("-")
        num, den = abs(numerator), abs(denominator)

        # add integral part into string 
        div, rmd = divmod(num, den)
        res.append(str(div))

        # no numbers after decimal 
        if not rmd: 
            pass 

        # numbers after decimal
        else:
            
            dec_vals = dict()
            res.append(".")

            while rmd:
                
                # recurring decimal points
                if rmd in dec_vals:
                    
                    # we add the ( in the position according to length 
                    res.insert(dec_vals[rmd], "(")
                    res.append(")")
                    break
                
                # push length of result so far into dict with remainder as key 
                dec_vals[rmd] = len(res)
                div, rmd = divmod(rmd * 10, den)
                res.append(str(div))
        
        return "".join(res)

# @lc code=end