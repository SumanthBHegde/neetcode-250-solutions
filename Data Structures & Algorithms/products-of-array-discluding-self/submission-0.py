class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                total_prod *= n

        res = [0] * len(nums)

        # More than one zero
        if zero_count > 1:
            return res

        # Exactly one zero
        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = total_prod
            return res

        # No zeros
        for i in range(len(nums)):
            res[i] = total_prod // nums[i]

        return res