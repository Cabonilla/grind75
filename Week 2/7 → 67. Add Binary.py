class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, base=2) + int(b, base=2), 'b')