class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 0, 1
        
        for i in range(n):
            first, second = second, first + second
            
        return second