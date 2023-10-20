class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cntr = Counter(tasks)
        mxhp = [-cnt for cnt in cntr.values()]
        heapq.heapify(mxhp)

        clk = 0
        q = deque()

        while mxhp or q:
            clk += 1
            if mxhp:
                cnt = 1 + heapq.heappop(mxhp)
                if cnt:
                    q.append([cnt, clk + n])
            if q and q[0][1] == clk:
                heapq.heappush(mxhp, q.popleft()[0])
                
        return clk