class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        m_vol = 0
        while l<r:
            min_height = min(heights[l],heights[r])
            distance = r-l
            vol = min_height*distance
            m_vol = max(m_vol,vol)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return m_vol