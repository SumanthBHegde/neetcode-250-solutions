class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        s = 0
        l = float('inf')
        for j in range(len(nums)):

            s += nums[j]
            while s >= target:
                l = min(l, j - i + 1)
                s -= nums[i]
                i += 1
            
        return 0 if l == float('inf') else l