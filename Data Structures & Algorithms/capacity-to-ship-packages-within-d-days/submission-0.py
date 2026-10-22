class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l,r = max(weights), sum(weights)
        res = r

        def cap(m):
            n,cur = 1,m
            for w in weights:
                if cur-w < 0:
                    n += 1
                    cur = m
                cur -= w
            return n <= days

        while l<=r:
            mid = (l+r)//2
            
            if cap(mid):
                res = min(res,mid)
                r = mid -1
            else:
                l = mid+1
        
        return res