class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l,r = 0,len(height)-1
        m_l,m_r = 0,0
        res = 0
        while l<r:
            m_l = max(m_l,height[l])
            if m_l - height[l] > 0:
                res += m_l - height[l]

            m_r = max(m_r,height[r])
            if m_r - height[r] > 0:
                res += m_r - height[r]
            
            if m_l <= m_r:
                l+=1
            else:
                r -= 1
        return res
            