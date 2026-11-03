class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*(n+1)
        def stairs(step):

            if step == 0:
                return 1
            if step < 0:
                return 0
            
            if cache[step]!=-1:
                return cache[step]
            
            cache[step] = stairs(step-1) + stairs(step -2)
            return cache[step]

        return stairs(n)
