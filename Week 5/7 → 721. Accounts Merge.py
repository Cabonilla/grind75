class UnionFind:
    def __init__(self, ln):
        self.prnt = [i for i in range(ln)]
        self.rnk = [1] * ln
    def find(self, tar):
        # Essentially traversing the tree, switching off current nodes.
        while tar != self.prnt[tar]:
            self.prnt[tar] = self.prnt[self.prnt[tar]]
            tar = self.prnt[tar]
        return tar
    def union(self, ml1, ml2):
        p1, p2 = self.find(ml1), self.find(ml2)
        if p1 == p2:
            return False
        # Adopting smaller trees into larger ones.
        if self.rnk[p1] > self.rnk[p2]:
            self.prnt[p2] = p1
            self.rnk[p1] += self.rnk[p2]
        else:
            self.prnt[p1] = p2
            self.rnk[p2] += self.rnk[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        eml2acc = {}

        # Step 1: Unify existing emails.
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in eml2acc:
                    uf.union(i, eml2acc[e])
                else:
                    eml2acc[e] = i

        emlGrp = collections.defaultdict(list)
        
        # Step 2: Append same emails to leader (parent root).
        for e, i in eml2acc.items():
            ldr = uf.find(i)
            emlGrp[ldr].append(e)

        # Step 3: Return name and emails.
        res = []
        for i, e in emlGrp.items():
            name = accounts[i][0]
            res.append([name] + sorted(emlGrp[i]))
        
        return res