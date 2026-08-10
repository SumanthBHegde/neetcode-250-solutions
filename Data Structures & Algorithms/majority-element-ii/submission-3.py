class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        le = len(nums)
        l = []
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        for item in freq:
            if freq[item] > math.floor(le/3):
                l.append(item)
        return l