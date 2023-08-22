class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x:x[0] ** 2 + x[1] ** 2)[0:k]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []

        for x, y in points:
            d = math.sqrt(x ** 2 + y ** 2)
            if len(hp) < k:
                heappush(hp, (-d, [x,y]))
            else:
                heappushpop(hp, (-d, [x, y]))
        
        return [hp[i][1] for i in range(k)]