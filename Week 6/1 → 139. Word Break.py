class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ls = len(s) + 1
        # Tracks False values, changes to True if match.
        dp = [False] * ls
        # First value should be True, ending value should be True or False.
        dp[0] = True

        for i in range(1, ls):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]