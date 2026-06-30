class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        test = set(nums)
        m_res = 0
        for n in test:
            if n-1 not in test:
                res = 1

                while n + res in test:
                    res += 1
                m_res = max(m_res,res)
        return m_res