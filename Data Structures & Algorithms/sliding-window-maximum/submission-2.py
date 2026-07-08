class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        m = -float('inf')
        l = 0
        for i in range(k):
            m = max(m,nums[i])
        res.append(m)
        if k==1:
            return nums
        for r in range(k,len(nums)):
            if nums[l] == m:
                m = max(nums[l+1:r+1])
            m = max(m,nums[r])
            res.append(m)
            l+=1
        return res
            