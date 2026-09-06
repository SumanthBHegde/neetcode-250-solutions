class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low  = 1

        while low<high:
            hour = 0
            k = (low+high)//2
            for pile in piles:
                hour += (pile -1 +k) //k

            if hour<=h:
                high = k
            else:
                low = k+1
        return low