class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mSum = nums[0]
        s = nums[0]
        for i in range(1, len(nums)):
            s = max(nums[i],nums[i]+s)
            mSum = max(mSum, s)
        return mSum
            