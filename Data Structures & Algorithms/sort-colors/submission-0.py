class Solution:
    def sortColors(self, nums: List[int]) -> None:

        def partition(low, high):
            pivot = nums[low]
            i = low + 1
            j = high

            while True:
                while i <= high and nums[i] < pivot:
                    i += 1

                while j >= low and nums[j] > pivot:
                    j -= 1

                if i >= j:
                    break

                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

            nums[low], nums[j] = nums[j], nums[low]
            return j

        def quicksort(low, high):
            if low >= high:
                return

            p = partition(low, high)
            quicksort(low, p - 1)
            quicksort(p + 1, high)

        quicksort(0, len(nums) - 1)