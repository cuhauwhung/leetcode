#
# @lc app=leetcode id=735 lang=python3
#
# [735] aCollision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids):
        
        # key: use a stack 

        res = []
        for ast in asteroids:
            if ast > 0:
                res.append(ast)

            elif ast < 0:

                # While top of the stack is positive.
                while res and res[-1] > 0:
                    # Both asteroids are equal, destroy both.
                    if res[-1] == -ast: 
                        res.pop()
                        break

                    # Stack top is smaller, remove the +ve ast
                    # from the stack and continue the comparison.
                    elif res[-1] < -ast:
                        res.pop()
                        continue

                    # Stack top is larger, -ve ast destroyed.
                    elif res[-1] > -ast:
                        break
                else:
                    # -ve made it all the way to the 
                    # bottom of the stack and destroyed all asteroids.
                    res.append(ast)

        return res

        
# @lc code=end

