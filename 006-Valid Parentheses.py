class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, parentheses = [], {"(":")", "[":"]", "{":"}"}
        for par in s:
            if par in parentheses:
                stack.append(par)
            elif len(stack) == 0 or par != parentheses[stack.pop()]:
                return False
        return len(stack) == 0