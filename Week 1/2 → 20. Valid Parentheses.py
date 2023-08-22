class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stk = []

        for i in s:
            if i in dct.keys():
                stk.append(i)

            elif len(stk) <= 0 or dct.get(stk.pop()) != i:
                return False

        return len(stk) != 1