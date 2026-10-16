class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        l,r = 0, x
        while l<=r:
            mid = (l+r)//2
            sq = 0
            for _ in range(mid):
                sq+=mid
                if sq > x:
                    break
            
            if sq == x:
                return mid
            elif sq<x:
                res = mid
                l = mid+1
            else:
                r = mid-1

        return res    

