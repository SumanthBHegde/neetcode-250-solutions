class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        k %= len(nums)
        n = len(nums) - 1

        reverse(0, n)
        reverse(0, k - 1)
        reverse(k, n)