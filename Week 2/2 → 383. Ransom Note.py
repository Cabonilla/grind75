class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rnsm = Counter(ransomNote)
        for i in rnsm:
            if i in magazine:
                if magazine.count(i) >= ransomNote.count(i):
                    return True

            return False

        return False