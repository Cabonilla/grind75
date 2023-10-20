class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        grph = defaultdict(set)

        for nde, edg in edges:
            grph[nde].add(edg)
            grph[edg].add(nde)

        lves = [nde for nde in grph if len(grph[nde]) == 1]

        while n > 2:
            n -= len(lves)
            bnk = []
            for lf in lves:
                nbr = grph[lf].pop()
                grph[nbr].remove(lf)
                if len(grph[nbr]) == 1:
                    bnk.append(nbr)
            lves = bnk
        
        return lves