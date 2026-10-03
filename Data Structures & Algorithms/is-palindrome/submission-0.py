class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([val for val in s if val.isalpha() or val.isnumeric()])
        if s.lower() == s.lower()[::-1]:
            return True
        else:
            return False