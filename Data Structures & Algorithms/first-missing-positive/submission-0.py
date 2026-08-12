class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n  and nums[i] != nums[nums[i]-1]:
                index = nums[i] - 1
                nums[i],nums[index] = nums[index],nums[i]
        
        for j in range(n):
            if nums[j] != j+1:
                return j+1
        return n+1