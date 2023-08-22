class Solution:
    def isPalindrome(self, s: str) -> bool:
        strng = [i.lower() for i in s if i.isalnum()]
        return ''.join(strng) == ''.join(strng)[::-1]