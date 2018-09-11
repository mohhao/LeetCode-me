class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == self.reverse(x):
            return True
        else:
            return False
        
    def reverse(self, x):
        result = 0
        while x:
            result = result*10 + x%10
            x = x// 10
        return result if result<=0x7fffffff else 0