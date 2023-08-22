class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nch, ch, c = -1, 0, 1
        status = [nch for _ in range(numCourses)]
        reqs = collections.defaultdict(list)

        for crs, pcrs in prerequisites:
            reqs[crs].append(pcrs)

        def conflict(crs):
            if status[crs] != nch:
                return status[crs] == ch

            status[crs] = ch

            for pcrs in reqs[crs]:
                if conflict(pcrs):
                    return True

            status[crs] = c

            return False

        for crs_idx in range(numCourses):
            if conflict(crs_idx):
                return False

        return True
