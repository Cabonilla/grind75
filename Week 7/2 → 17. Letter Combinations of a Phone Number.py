class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        
        if not digits:
            return ans

        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def bktrk(cmbo, nxt):
            if len(nxt) == 0:
                ans.append(cmbo)
            else:
                for ltr in map[nxt[0]]:
                    bktrk(cmbo + ltr, nxt[1:])

        bktrk("", digits)
        return ans