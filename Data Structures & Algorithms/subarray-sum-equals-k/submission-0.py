class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        freq = {0:1}
        pref = 0
        for n in nums:
            pref += n
            if pref - k in freq:
                count += freq[pref-k]
            freq[pref] = freq.get(pref,0) + 1
        
        return count
