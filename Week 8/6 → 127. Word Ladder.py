from collections import defaultdict, deque
from types import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # hot dot etc...
        # ||| |||
        # *ot *ot <
        # h*t d*t
        # ho* do*
        
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        lbw = len(beginWord)
        bnk = defaultdict(list)

        for w in wordList:
            for i in range(lbw):
                bnk[w[:i] + "*" + w[i + 1:]].append(w)

        q = deque([(beginWord, 1)])
        seen = set()
        seen.add(beginWord)

        while q:
            curr, lvl = q.popleft()
            for i in range(lbw):
                mid = curr[:i] + "*" + curr[i + 1:]
                for w in bnk[mid]:
                    if w == endWord:
                        return lvl + 1
                    if w not in seen:
                        seen.add(w)
                        q.append((w, lvl + 1))

        return 0