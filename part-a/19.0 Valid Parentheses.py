# Question: https://leetcode.com/problems/valid-parentheses/description/

# Beats 99%

class Solution:
    def isValid(self, s):
        stack, dict = [], {")": "(", "]": "[", "}": "{"}
        for bracket in s:
            if bracket not in dict:
                stack.append(bracket)
            else:
                if stack != [] and dict[bracket] == stack.pop():
                    continue
                else:
                    return False
        return True if stack == [] else False
