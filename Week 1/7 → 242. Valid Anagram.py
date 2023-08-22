class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sts = set(s)
        if len(s) != len(t):
            return False

        for i in sts:
            if s.count(i) != t.count(i):
                return False

        return True