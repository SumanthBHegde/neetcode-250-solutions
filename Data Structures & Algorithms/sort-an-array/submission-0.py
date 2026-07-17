class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def divide(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = divide(arr[:mid])
            right = divide(arr[mid:])

            merged = [0] * (len(left) + len(right))
            merge(left, right, merged)

            return merged

        def merge(a, b, c):
            i = j = k = 0

            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    c[k] = a[i]
                    i += 1
                else:
                    c[k] = b[j]
                    j += 1
                k += 1

            while i < len(a):
                c[k] = a[i]
                i += 1
                k += 1

            while j < len(b):
                c[k] = b[j]   # <-- this was your bug
                j += 1
                k += 1

        return divide(nums)